import numpy as np
N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
A = np.sort(A)

G = A[A > 0]
Z = A[A == 0]
L = A[A < 0]

l, r = 10**18, -10**18

while l - r > 1:
    m = (l + r) // 2

    Pk = np.searchsorted(A, m // G, side="right").sum()

    Nk = (N - np.searchsorted(A, (-m - 1) // (-L), side="right")).sum()

    duplicate = np.count_nonzero(A * A <= m)

    Zk = 0
    if m >= 0:
        Zk += len(Z) * N

    k = Pk + Nk + Zk - duplicate

    k //= 2

    if k >= K:
        l = m
    else:
        r = m
print(l)
