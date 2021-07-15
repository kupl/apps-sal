# まずワーシャルフロイドの表を作る
# 元の表で頂点A-Bを結ぶ距離が、ワーシャルフロイドの表で短縮されていたら、その辺は使わないで良いことになる
# この個数を数える

import sys
readline = sys.stdin.readline

import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import csgraph_from_dense

N,M = map(int,readline().split())

INF = 10 ** 9
G = [[INF] * N for i in range(N)]
for i in range(M):
  a,b,c = map(int,readline().split())
  G[a-1][b-1] = c
  G[b-1][a-1] = c

d = csgraph_from_dense(G, null_value=10**9)
d = floyd_warshall(d)

ans = 0
for a in range(N-1):
  for b in range(a + 1,N):
    if G[a][b] == INF:
      continue
    if G[a][b] > d[a][b]:
      ans += 1
      
print(ans)
