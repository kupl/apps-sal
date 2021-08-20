import numpy as np
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)
a = np.array(a)
f = np.array(f)
low = -1
hi = 10 ** 18
while hi - low > 1:
    ave = (hi + low) // 2
    if np.maximum(0, a - ave // f).sum() <= k:
        hi = ave
    else:
        low = ave
print(hi)
