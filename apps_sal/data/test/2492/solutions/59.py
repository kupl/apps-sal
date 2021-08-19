import numpy as np
(n, k) = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
a.sort()
p = a[a > 0]
z = np.count_nonzero(a == 0)
m = a[a < 0]
r = 10 ** 19
l = -r
while r - l > 1:
    b = (l + r) // 2
    c = 0
    if b >= 0:
        c += z * n
    c += a.searchsorted(b // p, side='right').sum()
    c += n * len(m) - a.searchsorted(-(-b // m), side='left').sum()
    c -= np.count_nonzero(a * a <= b)
    if c // 2 >= k:
        r = b
    else:
        l = b
print(r)
