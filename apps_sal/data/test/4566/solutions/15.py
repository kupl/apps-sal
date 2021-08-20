import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce


def rr():
    return sys.stdin.readline().rstrip()


def rs():
    return sys.stdin.readline().split()


def ri():
    return int(sys.stdin.readline())


def rm():
    return list(map(int, sys.stdin.readline().split()))


def rl():
    return list(map(int, sys.stdin.readline().split()))


inf = float('inf')
mod = 10 ** 9 + 7
(n, m) = rm()
li = [[] for _ in range(n)]
for _ in range(m):
    (a, b) = rm()
    a -= 1
    b -= 1
    li[a].append(b)
    li[b].append(a)
for lis in li:
    print(len(lis))
