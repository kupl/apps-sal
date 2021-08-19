import numpy as np
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a = np.array(a)
a.sort()
plus = a[a > 0]
zero = np.count_nonzero(a == 0)
minus = a[a < 0]
low = -10 ** 20
hi = 10 ** 20
while hi - low > 1:
    item = 0
    ave = (hi + low) // 2
    if ave >= 0:
        item += zero * n
    item += a.searchsorted(ave // plus, side='right').sum()
    item += n * len(minus) - a.searchsorted(-(-ave // minus), side='left').sum()
    item -= np.count_nonzero(a * a <= ave)
    if item // 2 >= k:
        hi = ave
    else:
        low = ave
print(hi)
