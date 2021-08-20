from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
import pprint
from typing import Union
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


n = inp()
s = list(input())
res = []
for (i, x) in enumerate(s):
    res.append(x)
    ln = len(res)
    if ln >= 3 and res[ln - 3:ln] == ['f', 'o', 'x']:
        for _ in range(3):
            res.pop()
print(len(res))
