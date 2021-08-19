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


n = INT()
a = LIST()
b = [0] * n
k = 0
for i in range(n // 2):
    k += a[2 * i + 1] - a[2 * i]
b[0] = a[n - 1] - k
b[n - 1] = a[n - 1] + k
for i in range(1, n - 1):
    b[i] = 2 * a[i - 1] - b[i - 1]
print(*b)
