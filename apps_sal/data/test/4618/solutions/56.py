import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7

s = input()
K = INT()


substr = []

for l in range(len(s)):
    r = l + 1
    while r < len(s) + 1:
        if bisect(substr, s[l:r]) == 5:
            break
        elif s[l:r] in substr:
            r += 1
        elif s[l:r] not in substr:
            insort(substr, s[l:r])
            substr = substr[:5]
            if s[l:r] in substr:
                r += 1


print((substr[K - 1]))
