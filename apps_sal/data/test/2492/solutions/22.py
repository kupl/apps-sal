import numpy as np
n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))

a.sort()

plus = a[a > 0]
minus = a[a < 0]
zero = a[a == 0]

#infだと割ってもinf
left = -10 ** 18
right = 10 ** 18

while left + 1 < right:
    x = (left + right) // 2
    cnt = 0
    if x >= 0:
        cnt += n * len(zero)
    cnt += a.searchsorted(x // plus, side="right").sum()
    cnt += (n - a.searchsorted(-(-x // minus), side="left")).sum()
    cnt -= np.count_nonzero(a * a <= x)
    cnt //= 2

    if cnt >= k:
        right = x
    else:
        left = x

print(right)

