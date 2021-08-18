from bisect import bisect_left
from itertools import accumulate
import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return list(map(int, input().split()))
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int, input().split()))
def lcm(a, b): return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 9)
mod = 10**9 + 7
cnt = 0
ans = 0
inf = float("inf")

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [0] + list(accumulate(a))


ans = 0
for i in range(n + 1):
    j = bisect_left(a, k + a[i])
    ans = ans + n - j + 1
print(ans)
