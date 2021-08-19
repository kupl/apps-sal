import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
N = INT()
l = [int(input()) for _ in range(N)]
c = Counter(l)
ans = 0
for (i, j) in zip(list(c.keys()), list(c.values())):
    if j % 2 != 0:
        ans += 1
print(ans)
