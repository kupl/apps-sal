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
def MAP(): return list(map(str, input().split()))
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
S = [_ for _ in input()]

left, right = 0, S[1:].count('E')
ans = left + right
for i in range(N-1):
    if S[i] == 'W':
        left += 1
    if S[i+1] == 'E':
        right -= 1

    ans = min(ans, left + right)

print(ans)

