from collections import deque
n, m = list(map(int, input().split()))
info = [list(map(int, input().split())) for i in range(m)]

# 重要な事実としてNの最大値×D_iの最大値はちょうど10^4*10^5 = 10^9 = 座標の幅。
# 「位置関係は全て正しく置けるが、0〜10^9に収まらないのでダメ」という可能性は考慮しなくて良い。
# 辺を通って到達可能か否かで分かれる。→幅優先か深さ優先かUnion-Findだな。
# 迷ったら幅優先で書こう。
# なおエッジを1本ずつ（入力された順に）処理するのはマズい。100個の点からなる塊が2つあって、最後にそれが2つの線で結ばれた場合、無矛盾かどうかどうやって判別するか?


nei = [[] for _ in range(n)]
for edge in info:
    v0 = edge[0] - 1
    v1 = edge[1] - 1
    nei[v0].append((v1, edge[2]))
    nei[v1].append((v0, -edge[2]))

queue = deque()
visited = [False] * n
pos = [None] * n

for i in range(n):
    if visited[i]:
        continue
    queue.append(i)

    pos[i] = 0  # 相対位置なので、値は何でも良い

    while len(queue) > 0:
        v = queue.popleft()
        visited[v] = True

        for n, diff in nei[v]:
            if pos[n] == None:
                pos[n] = pos[v] + diff
                queue.append(n)

            else:
                # 既に訪問済み→座標が決まっている→整合性チェック
                if pos[n] != pos[v] + diff:
                    print('No')
                    return

print('Yes')
