import math
import sys
from bisect import bisect_right, bisect_left
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate
from sys import stdout


def R():
    return map(int, input().split())


(hy, ay, dy) = R()
(hm, am, dm) = R()
(ch, ca, cd) = R()
res = math.inf
for ayp in range(1000):
    if ay + ayp > dm:
        k = (hm + ay + ayp - dm - 1) // (ay + ayp - dm)
        for dyp in range(1000):
            hyp = max(0, k * max(0, am - dy - dyp) - hy + 1)
            res = min(res, hyp * ch + dyp * cd + ayp * ca)
print(res)
