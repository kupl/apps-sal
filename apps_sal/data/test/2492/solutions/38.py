import numpy as np
(N, K) = list(map(int, input().split()))
A = np.sort(np.array(input().split(), np.int64))
z = A[A == 0]
p = A[A > 0]
n = A[A < 0]


def check(x):
    count = 0
    if x >= 0:
        count += len(z) * N
    count += np.searchsorted(A, x // p, side='right').sum()
    count += (N - np.searchsorted(A, (-x - 1) // -n, side='right')).sum()
    count -= np.count_nonzero(A * A <= x)
    assert count % 2 == 0
    count //= 2
    return count >= K


left = -10 ** 19
right = 10 ** 19
while right > left + 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)
