import numpy as np
(N, K) = [int(i) for i in input().split(' ')]
A = np.array([int(i) for i in input().split(' ')])
A.sort()
zero = A[A == 0]
minus = A[A < 0]
plus = A[A > 0]


def index_count(x):
    cnt = 0
    if x >= 0:
        cnt += len(zero) * N
    cnt += np.searchsorted(A, x // plus, side='right').sum()
    cnt += (N - np.searchsorted(A, -(-x // minus), side='left')).sum()
    cnt -= np.count_nonzero(A * A <= x)
    assert cnt % 2 == 0
    return cnt // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    mid = (left + right) // 2
    a = index_count(mid)
    if a >= K:
        right = mid
    else:
        left = mid
print(right)
