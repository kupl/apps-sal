import math
from collections import Counter, defaultdict
from itertools import accumulate


def R(): return map(int, input().split())


n, k = R()
ts = list(R()) + [-1]
k -= sum(1 if t < 0 else 0 for t in ts[:n])
res = 0 if ts[0] >= 0 else 1
for i in range(1, n):
    if ts[i - 1] < 0 and ts[i] >= 0 or ts[i - 1] >= 0 and ts[i] < 0:
        res += 1
locs = [i for i, t in enumerate(ts) if t < 0]
ps = sorted((y - x - 1, y) for x, y in zip(locs, locs[1:]) if y - x > 1)
res1 = res
k1 = k
for p in ps:
    if k >= p[0]:
        res -= (2 if p[1] < n else 1)
        k -= p[0]
    if k1 >= p[0] and p[1] < n:
        res1 -= 2
        k1 -= p[0]
res = res if k >= 0 else math.inf
res1 = res1 if k1 >= 0 else math.inf
print(min(res, res1) if min(res, res1) < math.inf else -1)
