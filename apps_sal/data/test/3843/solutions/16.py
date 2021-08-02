import math
import sys
from bisect import bisect_right, bisect_left, insort_right
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate, permutations, combinations
from sys import stdout


def R(): return map(int, input().split())


n, m = R()
nc, mc = n, m
n -= 1
m -= 1
a = b = 0
while n:
    n //= 7
    a += 1
while m:
    m //= 7
    b += 1
a, b = max(1, a), max(1, b)
if a + b > 7:
    print(0)
else:
    res = 0
    bs = [1]
    whole = [0, 1, 2, 3, 4, 5, 6]
    for i in range(10):
        bs.append(bs[-1] * 7)
    for pa in permutations(whole, a):
        if sum(x * y for x, y in zip(bs, pa)) < nc:
            for pb in permutations([x for x in whole if x not in pa], b):
                if sum(x * y for x, y in zip(bs, pb)) < mc:
                    res += 1
    print(res)
