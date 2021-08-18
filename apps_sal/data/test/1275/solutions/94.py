from operator import add, itemgetter, mul, xor
from math import gcd
from decimal import Decimal
from copy import deepcopy
from collections import Counter, defaultdict, deque
import math
import itertools
import heapq
import bisect
import sys
sys.setrecursionlimit(10**7)


def cmb(n, r, mod):
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
        bunshi = bunshi * (n - i) % mod
    return (bunshi * pow(bunbo, mod - 2, mod)) % mod


mod = 998244353
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return list(map(int, input().split()))
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


def func(n, k):
    return min(k - 1, 2 * n + 1 - k)


n, k = MI()
A = max(2, 2 + k)
B = min(2 * n, 2 * n + k)
ans = 0
for x in range(A, B + 1):
    ans += func(n, x) * func(n, x - k)
print(ans)
