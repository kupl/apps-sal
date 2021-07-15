import numpy as np
from scipy.sparse.csgraph import floyd_warshall

N = int(input())
A = np.asarray([[int(Aij) for Aij in input().split()] for _ in range(N)])

A2 = floyd_warshall(A, directed=False)

if np.any(A != A2):
    print(-1)
else:
    d = 0
    A += np.diag([2*10**9] * N)
    for i in range(N):
        for j in range(i + 1, N):
            if np.min(A[i] + A[j]) != A[i, j]:
                d += A[i, j]
    print(d)
