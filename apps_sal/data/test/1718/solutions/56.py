from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
import pprint
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


(n, k) = inpl()
a = inpl()
now = 0
res = 0
for x in a:
    if x != 1:
        now += 1
    if now == k - 1:
        res += 1
        now = 0
if now:
    res += 1
print(res)
