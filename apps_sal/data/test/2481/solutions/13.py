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


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(MAP())


(h, w) = MAP()
c = []
for i in range(10):
    c.append(LIST())
a = []
for i in range(h):
    a.append(LIST())
chk = True
while chk:
    chk = False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if c[i][j] > c[i][k] + c[k][j]:
                    c[i][j] = c[i][k] + c[k][j]
                    chk = True
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += c[a[i][j]][1]
print(ans)
