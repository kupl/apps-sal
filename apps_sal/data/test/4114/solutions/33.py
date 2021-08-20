from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf
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
x = [0] * n
y = [0] * n
h = [0] * n
for i in range(n):
    (x[i], y[i], h[i]) = MAP()
for i in range(101):
    for j in range(101):
        H = 0
        for k in range(n):
            if h[k] != 0:
                if H == 0 or H == h[k] + abs(x[k] - i) + abs(y[k] - j):
                    H = h[k] + abs(x[k] - i) + abs(y[k] - j)
                else:
                    break
        else:
            for k in range(n):
                if h[k] == 0:
                    if H - abs(x[k] - i) - abs(y[k] - j) <= 0:
                        continue
                    else:
                        break
            else:
                print(i, j, H)
