import sys
import re
import os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def S_MAP():
    return map(str, input().split())


def LIST():
    return list(map(int, input().split()))


def S_LIST():
    return list(map(str, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
N = INT()
A = LIST()
S = set(A)
C = Counter(A)
cnt = 0
for s in S:
    if C[s] != s:
        if C[s] > s:
            cnt += C[s] - s
        else:
            cnt += C[s]
print(cnt)
