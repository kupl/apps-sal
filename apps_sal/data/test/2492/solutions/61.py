import numpy as np
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = np.array(a, dtype="int64")
a_minus = a[a < 0]
a_plus = a[a > 0]
a_zero = a[a == 0]
l = - 10**19
r = 10**19


while r - l > 1:
    mid = (l + r) // 2
    cnt = 0
    cnt += a.searchsorted(mid // a_plus, side="right").sum()
    cnt += (n - a.searchsorted((-mid - 1) // (-a_minus), side="right")).sum()
    cnt -= np.count_nonzero(a * a <= mid)
    cnt += len(a_zero) * n if mid >= 0 else 0

    cnt //= 2

    if cnt >= k:
        r = mid
    else:
        l = mid

print(r)
