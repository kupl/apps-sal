from scipy.sparse.csgraph import *
import numpy as np
(N, M) = map(int, input().split())
E = [list(map(int, input().split())) for m in range(M)]
G = np.zeros((N, N))
ans = 0
for (a, b, c) in E:
    G[a - 1][b - 1] = c
    G[b - 1][a - 1] = c
F = shortest_path(G).astype(int)
for (a, b, c) in E:
    if F[a - 1][b - 1] != c:
        ans += 1
print(ans)
