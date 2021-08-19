from scipy.sparse.csgraph import floyd_warshall
import numpy as np
from itertools import permutations, combinations
(n, m, R) = map(int, input().split())
r = list(map(int, input().split()))
for i in range(R):
    r[i] -= 1
d = np.zeros((n, n))
for i in range(m):
    (a, b, c) = map(int, input().split())
    (a, b) = (a - 1, b - 1)
    d[a, b] = c
dist = floyd_warshall(d, directed=0).astype(int)
ans = 10 ** 10
for v in permutations(r):
    tmp = 0
    for i in range(R - 1):
        tmp += dist[v[i], v[i + 1]]
    ans = min(ans, tmp)
print(ans)
