import itertools
import numpy as np

N, K = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
A = np.sort(A)

positive = A[A > 0]
negative = A[A < 0]
zero = A[A == 0]

l = -10**18
r = 10**18

while l + 1 < r:
    x = (l + r) // 2
    cnt = 0
    if x >= 0:
        cnt += N * len(zero)

    cnt += A.searchsorted(x // positive, side="right").sum()
    cnt += (N - A.searchsorted(-(-x // negative), side="left")).sum()
    cnt -= np.count_nonzero(A * A <= x)
    cnt //= 2

    if cnt >= K:
        r = x
    else:
        l = x
print(r)
