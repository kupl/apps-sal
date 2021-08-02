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
def LIST1(): return list(MAP1())


def solve():
    N = INT()
    a = []
    b = []
    for i in range(N):
        A, B = MAP()
        a.append(A)
        b.append(B)
    a.sort()
    b.sort()

    if N % 2 == 1:
        am = a[(N + 1) // 2 - 1]
        bm = b[(N + 1) // 2 - 1]
        ans = bm - am + 1
    else:
        am = (a[N // 2 - 1] + a[N // 2]) / 2
        bm = (b[N // 2 - 1] + b[N // 2]) / 2
        ans = int((bm - am) * 2 + 1)
    print(ans)


def __starting_point():
    solve()


__starting_point()
