import numpy as np
(N, K) = map(int, input().split())
a = np.array(input().split(), np.int64)
a = np.sort(a)
zero = a[a == 0]
pos = a[a > 0]
neg = a[a < 0]


def f(x):
    count = 0
    c = x // pos
    count += np.searchsorted(a, c, side='right').sum()
    count += N * len(zero) if x >= 0 else 0
    c = -(-x // neg)
    count += (N - np.searchsorted(a, c, side='left')).sum()
    count -= a[a * a <= x].size
    count //= 2
    return count


right = 10 ** 18
left = -10 ** 18
while right - left > 1:
    mid = (right + left) // 2
    if f(mid) < K:
        left = mid
    else:
        right = mid
print(right)
