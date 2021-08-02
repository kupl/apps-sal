import bisect
import numpy as npy
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
n0, np, nn = 0, 0, 0
for i in a:
    if i > 0: np += 1
    elif i == 0: n0 += 1
    else: nn += 1
kp = (np**2 - np + nn**2 - nn) // 2
k0 = n0 * (n - n0) + (n0**2 - n0) // 2
kn = nn * np
if kn < k <= kn + k0:
    print(0)
    return
nls = []
pls = []
for i in range(n):
    if a[i] < 0:
        nls.append(a[i])
    elif a[i] > 0:
        pls.append(a[i])
ln = len(nls)
lp = len(pls)
nls = npy.array(nls, dtype=npy.int64)
pls = npy.array(pls, dtype=npy.int64)
if k <= kn:
    l = a[0] * a[-1] - 1
    r = 0
    while l + 1 < r:
        m = (l + r) // 2
        mls = m // nls
        tmp = npy.searchsorted(pls, mls, side="right").sum()
        if tmp > kn - k:
            l = m
        else:
            r = m
    print(l)
else:
    nls = -nls
    nls = nls[::-1]
    k -= kn + k0
    l = 0
    r = max(a[0]**2, a[-1]**2) + 1
    while l + 1 < r:
        m = (l + r) // 2
        tmp = npy.searchsorted(nls, m // nls, side="right").sum()
        tmp += npy.searchsorted(pls, m // pls, side="right").sum()
        tmp -= npy.searchsorted(nls**2, m, side="left")
        tmp -= npy.searchsorted(pls**2, m, side="left")
        if tmp >= 2 * k:
            r = m
        else:
            l = m
    print(r)
