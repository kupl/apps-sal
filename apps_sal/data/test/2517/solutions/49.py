import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
from itertools import permutations

n,m,R = map(int, input().split())
r = list(map(int, input().split()))
r = [i-1 for i in r]
abc = [list(map(int, input().split())) for i in range(m)]
edge = [[10 ** 9] * (n) for i in range(n)]
for a,b,c in abc:
  a-=1
  b-=1
  edge[a][b] = c
  edge[b][a] = c
d = floyd_warshall(edge)
ans = 10 ** 18
for i in permutations(r):
  tmp = 0
  for j in range(R-1):
    tmp += d[i[j]][i[j+1]]
  ans = min(ans,tmp)
print(int(ans))
