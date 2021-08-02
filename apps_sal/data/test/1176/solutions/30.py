import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
A = LIST()

cnt = 0
for a in A:
    if a < 0:
        cnt += 1

if cnt % 2 == 0:
    B = [abs(a) for a in A]
    ans = sum(B)
else:
    C = [abs(a) for a in A]
    C_min = min(C)
    C_min_id = C.index(C_min)

    C[C_min_id] = C[C_min_id] * (-1)
    ans = sum(C)
print(ans)
