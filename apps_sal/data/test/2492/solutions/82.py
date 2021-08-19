import numpy as np
(n, k) = list(map(int, input().split()))
A = np.array(input().split(), np.int64)
A.sort()
zero = A[A == 0]
neg = A[A < 0]
pos = A[A > 0]


def f(x):
    cnt = 0
    if x >= 0:
        cnt += len(zero) * n
    cnt += A.searchsorted(x // pos, side='right').sum()
    cnt += (n - A.searchsorted(-(-x // neg), side='left')).sum()
    cnt -= np.count_nonzero(A * A <= x)
    return cnt // 2


l = -10 ** 18
r = 10 ** 18
while l < r:
    pov = (l + r) // 2
    if f(pov) >= k:
        r = pov
    else:
        l = pov + 1
print(l)
