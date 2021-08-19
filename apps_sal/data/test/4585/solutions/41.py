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
    return list(map(int, input().split()))


def S_MAP():
    return list(map(str, input().split()))


def LIST():
    return list(map(int, input().split()))


def S_LIST():
    return list(map(str, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
X = INT()
A = []
for i in range(1, 2 * (int(sqrt(X)) + 1)):
    a = i * (i + 1) // 2
    if a <= X:
        A.append(a)
    else:
        ans = len(A)
        mi = A.pop()
        ma = a
        break
if mi == X:
    print(ans)
else:
    print(ans + 1)
