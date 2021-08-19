from scipy.sparse.csgraph import csgraph_from_dense
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import shortest_path
import numpy as np
import sys
readline = sys.stdin.readline
(N, M) = map(int, readline().split())
INF = 10 ** 9
G = [[INF] * N for i in range(N)]
for i in range(M):
    (a, b, c) = map(int, readline().split())
    G[a - 1][b - 1] = c
    G[b - 1][a - 1] = c
d = csgraph_from_dense(G, null_value=10 ** 9)
d = floyd_warshall(d)
ans = 0
for a in range(N - 1):
    for b in range(a + 1, N):
        if G[a][b] == INF:
            continue
        if G[a][b] > d[a][b]:
            ans += 1
print(ans)
