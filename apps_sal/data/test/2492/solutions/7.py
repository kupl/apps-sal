
import numpy as np
n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
a.sort()
posi = a[a > 0]
zero = a[a == 0]
nega = a[a < 0]
l = -10**18 - 1
r = 10**18 + 1
while r - l > 1:
    mid = (r + l) // 2
    cnt = 0
    if mid >= 0:
        cnt += len(zero) * n

    cnt += a.searchsorted(mid // posi, side="right").sum()
    cnt += (n - a.searchsorted(-(-mid // nega), side="left")).sum()
    cnt -= np.count_nonzero(a * a <= mid)
    cnt //= 2
    if cnt >= k:
        r = mid
    else:
        l = mid
print(r)
