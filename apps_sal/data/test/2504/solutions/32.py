import sys
from scipy.sparse.csgraph import floyd_warshall

N, M, L = map(int, input().split())
INF = 10 **9 +1
G = [[float('inf')] * N for i in range(N)]
for i in range(M):
  a, b, c = map(int, input().split())
  a, b, = a - 1, b -1
  G[a][b] = c
  G[b][a] = c

#全点間最短距離を計算
G = floyd_warshall(G)


#コストL以下で移動可能な頂点間のコスト1の辺を張る
E = [[float('inf')] * N for i in range(N)]
for i in range(N):
  for j in range(N):
    if G[i][j] <= L:
      E[i][j] = 1

#全点間最短距離を計算
E = floyd_warshall(E)

#クエリに答えていく
Q = int(input())
for i in range(Q):
  s, t = map(int, input().split())
  s, t = s - 1, t-1
  print(int(E[s][t] - 1) if E[s][t] != float('inf') else -1)
