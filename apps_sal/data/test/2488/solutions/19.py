from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce, lru_cache
import string
import sys
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def MAP1():
    return map(lambda x: int(x) - 1, input().split())


def LIST():
    return list(MAP())


def LIST1():
    return list(MAP1())


def is_ok(arg):
    return h[arg][0] <= h[i][0] + d * 2


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


(n, d, a) = MAP()
h = [LIST() + [0] for i in range(n)]
h = sorted(h, key=itemgetter(0))
attack = 0
ans = 0
for i in range(n):
    bomb = ceil((h[i][1] - attack) / a)
    if bomb > 0:
        j = min(meguru_bisect(n, i), n - 1)
        h[j][2] -= bomb
        attack += bomb * a
        ans += bomb
    attack += h[i][2] * a
print(ans)
