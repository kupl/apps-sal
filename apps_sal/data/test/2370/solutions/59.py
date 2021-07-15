from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

import numpy as np

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a = np.array(a)

g = csr_matrix(a)
dist = floyd_warshall(g)

bl = dist == a

if bl.all():
    sm = dist.sum()
    INF = 10 ** 18 + 1
    inf = np.array([INF] * n)
    inf = np.diag(inf)
    dist += inf
    for u in range(n):
        for v in range(n):
            if u == v:
                continue

            mn = np.min(dist[u] + dist[v])
            if mn == dist[u, v]:
                sm -= dist[u, v]

    ans = int(sm) // 2
    print(ans)

else:
    print((-1))

