from heapq import heappush, heappop, heapify
n, m, s = list(map(int, input().split()))

# 所持銀が2500超えたら、2500になるまで銀貨捨てる
# 2500枚以上のDP表を作ると、かなりのメモリ消費するし、このケースでは2500枚あればどこでも行けるので意味ない
s = min(s, 2500)

# 2501×nの[]行列
# 0~2500枚 × 頂点数
edge = [[[] for i in range(50 * 50 + 1)] for i in range(n)]

# (頂点, コスト)→(頂点, コスト)へ辺を渡っての遷移（頂点が変わる）
# u,v,a,bが与えられるたびに、edgeを更新
for i in range(m):
    u, v, a, b = list(map(int, input().split()))

    # jは、保有銀貨枚数
    # j:a→2500なのは、jがa未満であれば、隣の頂点に行けないから
    for j in range(a, 2501):
        edge[u - 1][j].append((v - 1, j - a, b))
        edge[v - 1][j].append((u - 1, j - a, b))

# (頂点, コスト)→(頂点, コスト)へ、その頂点に留まって両替の遷移（頂点変わらない）
# c,dが与えられるたびに、edgeを更新
for i in range(n):
    c, d = list(map(int, input().split()))

    # 銀貨を捨てるのはノーコスト
    # 2500枚以上持ってたら、2500枚持ってることと同値と考える
    # range(2501)にしない理由は、2500枚あったら、両替はしないから
    for j in range(2500):
        if j + c >= 2500:
            edge[i][j].append((i, 2500, d))
        elif j + c < 2500:
            edge[i][j].append((i, j + c, d))


# dはn×2501のすべての状態の最小コストの表
d = [[float('inf') for i in range(50 * 50 + 1)] for i in range(n)]

# 初期値。頂点0, 銀貨Sには、コスト0で到達
d[0][s] = 0

pq = []
heappush(pq, (0, 0, s))

while len(pq):
    # [コスト, 頂点, 銀貨数]で、コストをkeyとして、heapソートして、一番コストが低いリストを先頭に持ってくる
    _, u, g = heappop(pq)

    # 頂点までのコストが更新できれば更新してヒープに登録
    # edge[u][g]は、頂点u, 銀貨g枚の状態から、行ける状態のtuple(頂点, 銀貨数, コスト)を呼び出す
    # pqには、[コスト, 頂点, 銀貨数]の順で入れている
    for tuple in edge[u][g]:
        if d[tuple[0]][tuple[1]] > d[u][g] + tuple[2]:
            d[tuple[0]][tuple[1]] = d[u][g] + tuple[2]
            heappush(pq, [d[u][g] + tuple[2], tuple[0], tuple[1]])

# d[i]で、頂点iにおける保有銀貨数に応じたコストが入ったリストを呼び出せる
# リストの中で、一番小さいコストのやつを呼び出せば、その頂点に行ける最小コストと同値である
for i in range(1, n):
    print((min(d[i])))
