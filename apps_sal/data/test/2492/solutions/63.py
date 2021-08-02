import numpy as np
N, K = list(map(int, input().split()))

A = np.array(list(map(int, input().split())))
A.sort()

pos = A[A > 0]
neg = A[A < 0]
zero = A[A == 0]

l = -10**18
r = 10**18

while l + 1 < r:
    x = (l + r) // 2
    cnt = 0
    if x >= 0:
        cnt += N * len(zero)

    cnt += A.searchsorted(x // pos, side="right").sum()
    cnt += (N - A.searchsorted(-(-x // neg), side="left")).sum()
    cnt -= np.count_nonzero(A * A <= x)
    cnt //= 2

    if cnt >= K:
        r = x
    else:
        l = x

print(r)
