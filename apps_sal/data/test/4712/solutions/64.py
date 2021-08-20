from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


(h, w) = inpl()
s = [input() for _ in range(h)]
res = []
for i in range(h + 2):
    if i == 0 or i == h + 1:
        res.append('#' * (w + 2))
    else:
        res.append('#' + s[i - 1] + '#')
for x in res:
    print(x)
