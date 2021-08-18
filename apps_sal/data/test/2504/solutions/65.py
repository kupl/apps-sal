import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m, l = map(int, input().split())
INF = 1 << 60

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if c > l:
        continue
    dist[a][b] = c
    dist[b][a] = c

dist = floyd_warshall(csr_matrix(dist))

dist2 = np.full_like(dist, 1)
dist2[np.where(dist > l)] = INF

dist2 = floyd_warshall(dist2, directed=False)
dist2 = dist2.astype(int)

dist2[dist2 == INF] = 0

q = int(input())

ans = []
for _ in range(q):
    s, t = map(int, input().split())
    ans.append(dist2[s - 1, t - 1] - 1)

print(*ans, sep="\n")
