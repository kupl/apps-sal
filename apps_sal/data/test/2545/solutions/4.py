from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** (-7)


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


def inpl_str():
    return list(sys.stdin.readline().split())


N = inp()
for _ in range(N):
    (a, b) = inpl()
    (a, b) = (min(a, b), max(a, b))
    a = b = a - (b - a)
    if a % 3 == 0 and a >= 0:
        print('YES')
    else:
        print('NO')
