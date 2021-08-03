import math
from bisect import bisect_right
from itertools import accumulate


def R(): return map(int, input().split())


n, p = R()
devs = []
for i in range(n):
    devs.append(tuple(R()))
devs = sorted(devs, key=lambda x: x[1] / x[0])
sp, sr, t = 0, 0, math.inf
for d in devs:
    sp += d[0]
    sr += d[1]
    if sp > p:
        t = min(t, sr / (sp - p))
print(t if t < math.inf else -1)
