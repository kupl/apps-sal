import sys
readline = sys.stdin.readline

import math

# 最短距離をワーシャルフロイドで求める
# 最短距離がL以下の街には燃料1で行けるので、辺を貼り直してワーシャルフロイド

N,M,L = map(int,readline().split())

import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import csgraph_from_dense
INF = 10 ** 9 + 1
G = [[INF for i in range(N)] for j in range(N)]
for i in range(M):
  a,b,c = map(int,readline().split())
  G[a - 1][b - 1] = c
  G[b - 1][a - 1] = c
G = csgraph_from_dense(G, null_value=INF)
d = floyd_warshall(G)

EG = [[INF for i in range(N)] for j in range(N)]
for i in range(N):
  for j in range(N):
    if d[i][j] <= L:
      EG[i][j] = 1

EG = csgraph_from_dense(EG, null_value=INF)
d = floyd_warshall(EG)

Q = int(readline())
for i in range(Q):
  s,t = map(int,readline().split())
  if d[s - 1][t - 1] != math.inf:
    print(int(d[s - 1][t - 1] - 1))
  else:
    print(-1)
