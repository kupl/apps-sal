import math
from bisect import bisect_right, bisect_left
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate


def R():
    return map(int, input().split())


t = int(input())
tab = [x * x * x for x in range(2, 2 * 10 ** 5)]
(l, r) = (1, 5 * 10 ** 15)
while l < r:
    n = (l + r) // 2
    s = sum((n // x for x in tab))
    if s < t:
        l = n + 1
    elif s > t:
        r = n - 1
    else:
        r = n
s = sum((l // x for x in tab))
if s != t:
    print(-1)
else:
    print(l)
