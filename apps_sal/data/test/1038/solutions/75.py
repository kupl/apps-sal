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


(a, b) = MAP()
a -= 1
s = deque()
tmp = (b + 1) // 2 - (a + 1) // 2
s.appendleft(str(tmp % 2))
i = 1
while 2 ** i <= b:
    x = max(0, a % 2 ** (i + 1) - (2 ** i - 1))
    y = max(0, b % 2 ** (i + 1) - (2 ** i - 1))
    tmp = y - x
    s.appendleft(str(tmp % 2))
    i += 1
t = list(s)
ans = ''.join(t)
print(int(ans, 2))
