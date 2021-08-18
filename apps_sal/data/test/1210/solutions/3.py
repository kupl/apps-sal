import re
import sys
import math
import string
import operator
import functools
import fractions
import collections
sys.setrecursionlimit(10**7)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
def RI(): return list(map(int, input().split()))
def RS(): return input().rstrip().split()


mod = 1e9 + 7
n, p = RI()
sharks = [0] * n
for i in range(n):
    l, r = RI()
    tot = (math.floor(r / p) - math.ceil(l / p) + 1)
    sharks[i] = 1 - tot / (r - l + 1)
ans = 0
for i in range(n):
    ans += (1 - (sharks[i]) * (sharks[i - 1]))
ans *= 2000
print(ans)
