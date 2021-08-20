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


(x, n) = inpl()
divs = set()
div = 2
while div * div <= x:
    while x % div == 0:
        divs.add(div)
        x //= div
    div += 1
if x != 1:
    divs.add(x)
ans = 1
for div in divs:
    tmp = 1
    while tmp <= n:
        tmp *= div
        ans *= pow(div, n // tmp, mod)
        ans %= mod
print(ans % mod)
