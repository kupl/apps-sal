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


def INPUT():
    return sys.stdin.readline().rstrip()


def INT():
    return int(INPUT())


def MAP():
    return list(map(int, INPUT().split()))


def S_MAP():
    return list(map(str, INPUT().split()))


def LIST():
    return list(map(int, INPUT().split()))


def S_LIST():
    return list(map(str, INPUT().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
N = INT()
A = LIST()
A_c = Counter(A)
ans = 0
for (k, v) in zip(list(A_c.keys()), list(A_c.values())):
    if k < v:
        ans += v - k
    elif k > v:
        ans += v
print(ans)
