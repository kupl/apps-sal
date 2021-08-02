from collections import deque
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
import itertools

n, m, r = map(int, input().split())
rlist = list(map(int, input().split()))
for i in range(r):
    rlist[i] -= 1
e = np.zeros((n, n), dtype=int)

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    e[a][b] = c
    e[b][a] = c
csr = csr_matrix(e)
f = floyd_warshall(csr)

ans = 10**18
for v in itertools.permutations(rlist, r):
    d = 0
    for i in range(r - 1):
        d += f[v[i]][v[i + 1]]
    ans = min(ans, d)
print(int(ans))
