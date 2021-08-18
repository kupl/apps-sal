from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
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
def LIST(): return list(MAP())


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - 2 - a[n - 1])


n, x = MAP()
a = [0] * n
p = [0] * n
a[0] = 1
p[0] = 1
for i in range(1, n):
    a[i] = a[i - 1] * 2 + 3
    p[i] = p[i - 1] * 2 + 1

print(f(n, x))
