import numpy as np
N, M, Q = map(int, input().split())
a = np.array([[0] * (N + 1) for i in range(N + 1)])
for i in range(M):
    l, r = map(int, input().split())
    a[l][r] += 1
a = a.cumsum(axis=0).cumsum(axis=1)
for i in range(Q):
    p, q = map(int, input().split())
    print(a[q][q] - a[p - 1][q] - a[q][p - 1] + a[p - 1][p - 1])
