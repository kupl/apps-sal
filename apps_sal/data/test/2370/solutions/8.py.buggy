import numpy as np
from scipy.sparse.csgraph import floyd_warshall as fw
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

a = fw(A)
ans = 0
for i in range(N):
    a[i][i] = np.inf
for i in range(N):
    for j in range(i):
        if A[i][j] != a[i][j]:
            print(-1)
            return
        else:
            if a[i][j] < np.min(a[i] + a[j]):
                ans += a[i][j]
print(int(ans))
