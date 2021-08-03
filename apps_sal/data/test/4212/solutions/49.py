from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def MAP1(): return map(lambda x: int(x) - 1, input().split())
def LIST(): return list(MAP())


def solve():
    N, M, Q = MAP()
    A = [LIST() for _ in range(Q)]

    ans = 0
    for x in combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for a, b, c, d in A:
            if x[b - 1] - x[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)


def __starting_point():
    solve()


__starting_point()
