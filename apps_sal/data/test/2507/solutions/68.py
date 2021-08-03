import math
import numpy as np


def yn(a, f, k, x):
    k_yt = np.maximum(np.zeros(a.shape), a - np.floor(np.divide(x, f)))
    k_yt = np.sum(k_yt)
    if k_yt <= k:
        return True
    else:
        return False


n, k = list(map(int, input().split()))
a = list((list(map(int, input().split()))))
f = list((list(map(int, input().split()))))
a.sort()
f.sort(reverse=True)
xo = max([a[i] * f[i] for i in range(n)])
a = np.array(a)
f = np.array(f)
# binary search
if xo == 0:
    print((0))
else:
    l = 0
    r = xo
    m = xo
    while l <= r:
        piv = int((r + l) / 2)
        if yn(a, f, k, piv):
            r = piv - 1
            m = piv
        else:
            l = piv + 1
    print(m)
