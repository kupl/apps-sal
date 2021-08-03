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
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(MAP())


a, b = MAP()


def f(n):
    if n % 2 == 1:
        if ((n + 1) // 2) % 2 == 1:
            return 1
        else:
            return 0
    else:
        if (n // 2) % 2 == 1:
            return n ^ 1
        else:
            return n


ans = f(a - 1) ^ f(b)
print(ans)
