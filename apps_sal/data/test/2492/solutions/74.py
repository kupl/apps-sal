import numpy as np

N, K = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
A.sort()
G = A[A > 0]
Z = A[A == 0]
L = A[A < 0]

ok = 10 ** 18 + 1
ng = -10 ** 18 - 1


while ok - ng > 1:
    mid = (ng + ok) // 2

    cg = np.searchsorted(A, mid // G, side="right").sum()

    cl = (N - np.searchsorted(A, (-mid - 1) // (-L), side="right")).sum()

    d = np.count_nonzero(A * A <= mid)

    z = 0
    if mid >= 0:
        z += len(Z) * N

    c = cg + cl + z - d

    c //= 2

    if c >= K:
        ok = mid
    else:
        ng = mid

print(ok)
