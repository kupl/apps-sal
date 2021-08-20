from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(MAP())


n = INT()
ls = []
for i in range(n - 1):
    (c, s, f) = MAP()
    ls.append([c, s, f])
for i in range(n - 1):
    ans = 0
    for j in range(i, n - 1):
        ans = max(ans, ls[j][1])
        ans = ls[j][0] + (ans + ls[j][2] - 1) // ls[j][2] * ls[j][2]
    print(ans)
print(0)
