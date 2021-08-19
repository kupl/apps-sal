import math
import sys
from bisect import bisect_right, bisect_left, insort_right
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate
from sys import stdout


def R():
    return map(int, input().split())


(n, m, d) = R()
a = sorted(((x, i) for (i, x) in enumerate(R())))
res = [-1] * len(a)
res[0] = 0
cnt = 0
q = [(a[0][0], 0)]
for r in range(1, n):
    h = heappop(q)
    if a[r][0] - h[0] > d:
        res[r] = h[1]
    else:
        cnt += 1
        res[r] = cnt
        heappush(q, h)
    heappush(q, (a[r][0], res[r]))
print(max(res) + 1)
for t in sorted(zip(a, res), key=lambda x: x[0][1]):
    print(t[1] + 1, end=' ')
