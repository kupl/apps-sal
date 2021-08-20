import sys
import numpy as np
(n, k) = map(int, input().split())
a = np.array(sorted(list(map(int, input().split()))))
f = np.array(sorted(list(map(int, input().split())), reverse=True))
asum = a.sum()
(l, r) = (0, 10 ** 13)
while l != r:
    mid = (l + r) // 2
    can = asum - np.minimum(mid // f, a).sum() <= k
    if can:
        r = mid
    else:
        l = mid + 1
print(l)
