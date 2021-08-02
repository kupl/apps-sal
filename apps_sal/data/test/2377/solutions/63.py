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

N, H = MAP()
A, B = [], []
for i in range(N):
    a, b = MAP()
    A.append(a)
    B.append(b)

max_a = max(A)
B = sorted(B, reverse=True)

ans = 0

for i in range(N):
    if max_a >= B[i]:
        ans += -(-H // max_a)
        H = 0
    else:
        H -= B[i]
        ans += 1
    if H <= 0:
        print(ans)
        break
if H > 0:
    ans += -(-H // max_a)
    print(ans)
