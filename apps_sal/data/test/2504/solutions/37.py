from scipy.sparse.csgraph import floyd_warshall
import numpy as np

N, M, L = map(int, input().split())

D = np.ones([N, N]) * np.inf
D[np.eye(N, dtype=bool)] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    D[A - 1, B - 1] = C
    D[B - 1, A - 1] = C

D = floyd_warshall(D)
D2 = (D <= L) * 1.0  # boolean -> float
D2[D2 == 0] = np.inf
# D2 = (D <= L) + (D > L)*np.inf

D2 = floyd_warshall(D2) - 1

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    r = D2[s - 1, t - 1]
    if r < np.inf:
        print(int(r))
    else:
        print(-1)
