import numpy as np

n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
a.sort()

zero = a[a == 0]
pos = a[a > 0]
neg = a[a < 0]

l = -10**18
r = 10**18

while l + 1 < r:
    x = (l + r) // 2
    cnt = 0

    if x >= 0:
        cnt += n * len(zero)

    cnt += a.searchsorted(x // pos, side='right').sum()
    cnt += (n - a.searchsorted(-(-x // neg), side='left')).sum()
    cnt -= np.count_nonzero(a * a <= x)
    cnt //= 2

    if cnt >= k:
        r = x
    else:
        l = x

print(r)
