from scipy.sparse.csgraph import floyd_warshall
import numpy as np
(N, M) = map(int, input().split())


def f(x):
    return (int(x[0]) - 1, int(x[1]) - 1, int(x[2]))


edges = list((f(input().split()) for _ in range(M)))
g = np.zeros((N, N), dtype=float)
for (a, b, c) in edges:
    g[a, b] = c
    g[b, a] = c
floyd_warshall(g, directed=False, overwrite=True)
res = sum((int(g[a, b] != c) for (a, b, c) in edges))
print(res)
