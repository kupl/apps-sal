import numpy as np
from scipy.sparse.csgraph import floyd_warshall
(N, M, L) = map(int, input().split())
gurahu = np.zeros((N, N))
for k in range(M):
    (a, b, c) = map(int, input().split())
    gurahu[a - 1, b - 1] = c
    gurahu[b - 1, a - 1] = c
gurahu = floyd_warshall(gurahu, directed=False)
gurahu = np.where((gurahu <= L) & (gurahu > 0), 1, 0)
gurahu = floyd_warshall(gurahu) - np.ones((N, N))
Q = int(input())
for k in range(Q):
    (s, t) = map(int, input().split())
    ans = gurahu[s - 1, t - 1]
    if ans == float('inf'):
        print(-1)
    else:
        print(int(ans))
