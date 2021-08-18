import numpy as np
n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
a.sort()

p = a[a > 0]
zeros = np.count_nonzero(a == 0)
m = a[a < 0]


def count(x):
    cnt = 0
    if x >= 0:
        cnt += zeros * n
    cnt += a.searchsorted(x // p, side='right').sum()
    cnt += n * len(m) - a.searchsorted(-(-x // m), side='left').sum()
    cnt -= np.count_nonzero(a * a <= x)
    return cnt // 2


l, r = -10**19, 10**19
while r - l > 1:
    mid = (r + l) // 2
    if count(mid) >= k:
        r = mid
    else:
        l = mid
print(r)
