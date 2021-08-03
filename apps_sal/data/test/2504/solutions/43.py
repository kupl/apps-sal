from scipy.sparse.csgraph import floyd_warshall
import numpy as np

N, M, L = list(map(int, input().split()))

D = np.ones([N, N]) * np.inf
D[np.eye(N, dtype=bool)] = 0

for _ in range(M):
    A, B, C = list(map(int, input().split()))
    D[A - 1, B - 1] = C
    D[B - 1, A - 1] = C

D = floyd_warshall(D)
D2 = D <= L

D2 = floyd_warshall(D2)

Q = int(input())
for _ in range(Q):
    s, t = list(map(int, input().split()))
    r = D2[s - 1, t - 1] - 1
    if r < np.inf:
        print((int(r)))
    else:
        print((-1))
