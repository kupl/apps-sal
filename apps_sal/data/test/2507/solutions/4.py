import numpy as np


def is_ok(mid, k):
    s = np.maximum(a - mid // f, 0).sum()
    if s <= k:
        return True
    else:
        return False


(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
a.sort()
f.sort(reverse=True)
a = np.array(a)
f = np.array(f)
(l, r) = (-1, np.max(a * f))
while l + 1 < r:
    mid = (l + r) // 2
    if is_ok(mid, k):
        r = mid
    else:
        l = mid
print(r)
