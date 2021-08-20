import math
import sys
from bisect import bisect_right, bisect_left, insort_right
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate, permutations, combinations
from sys import stdout


def R():
    return map(int, input().split())


n = int(input())
arr = list(R())
tps = [(0, 0)]
for x in arr:
    i = bisect_left(tps, (x, -1)) - 1
    tps.insert(i + 1, (x, tps[i][1] + 1))
    if i + 2 < len(tps) and tps[i + 1][1] >= tps[i + 2][1]:
        del tps[i + 2]
print(max((x[1] for x in tps)))
