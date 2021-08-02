from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

import numpy as np

n = int(input())
a = np.array([list(map(int, input().split())) for _ in range(n)])

g = csr_matrix(a)
dist = floyd_warshall(g)

if (dist == a).all():
    sm = dist.sum()

    INF = 10 ** 18 + 1
    for i in range(n):
        dist[i, i] = INF

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
