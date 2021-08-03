import math
import sys
from bisect import bisect_right, bisect_left
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate
from sys import stdout


def R(): return map(int, input().split())


np, nk, z = R()
ps = sorted(R())
ks = sorted(R())
res = math.inf
for ki in range(nk - np + 1):
    res = min(res, max(abs(x - y) + abs(y - z) for x, y in zip(ps, ks[ki:ki + np + 1])))
print(res)
