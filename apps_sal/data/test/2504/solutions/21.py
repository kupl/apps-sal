from scipy.sparse.csgraph import floyd_warshall

# ダイクストラではなくワーシャルフロイドで解く
N, M, L = list(map(int, input().split()))
# graph = [[] for _ in range(N)]
distant = [[float('inf')]*N for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a, b = a-1, b-1
    if c > L:
        continue
    distant[a][b] = c
    distant[b][a] = c

distant = floyd_warshall(distant)
another = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if distant[i][j] <= L:  # 行けるところまでいくという印象
            another[i][j] = 1
another = floyd_warshall(another)
Q = int(input())
for _ in range(Q):
    s, t = [int(x)-1 for x in input().split()]
    if another[s][t] == float('inf'):
        print((-1))
        continue
    print((int(another[s][t])-1))
    # if distant[s][t] == float('inf'):
    #     print(-1)
    #     continue
    # print(int(distant[s][t])//L + min(1, int(distant[s][t]) % L) - 1)
# 燃料が4で
# 1 -> 4 -> 2
# のとき、距離は7だから一見すると補給回数は1で良さそうだけど、実は2回必要
# 今、２点間の最小距離を求めておいて、もう一つのグラフは「最短距離がL以下の2点に辺(重み1)を張る」

