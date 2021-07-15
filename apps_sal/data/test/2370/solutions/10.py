import numpy as np
from scipy.sparse.csgraph import floyd_warshall

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

if np.any(A != floyd_warshall(A)):
    print((-1))
else:
    ans = 0
    A += np.diag([float('inf')] * N)
    for i in range(N):
        for j in range(i + 1, N):
            if np.min(A[i] + A[j]) != A[i, j]:
                ans += int(A[i, j])
    print(ans)

