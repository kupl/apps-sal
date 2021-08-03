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


def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
A = LIST()

A.sort(reverse=True)
ans = A[0]
cnt = 1

for x in A[1:]:
    if cnt == N - 1:
        break
    if cnt == N - 2:
        ans += x
        cnt += 1
        # 奇数の場合
    else:
        ans += 2 * x
        cnt += 2
print(ans)
