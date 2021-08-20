import numpy as np
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = np.array(a)
a.sort()
p = a[a > 0]
z = a[a == 0]
m = a[a < 0]
low = -10 ** 18
high = 10 ** 18
while high - low > 1:
    mid = (high + low) // 2
    count = 0
    if mid >= 0:
        count += len(z) * n
    count += a.searchsorted(mid // p, side='right').sum()
    count += (n - a.searchsorted(-(-mid // m), side='left')).sum()
    count -= np.count_nonzero(a * a <= mid)
    count /= 2
    if count >= k:
        high = mid
    if count < k:
        low = mid
print(high)
