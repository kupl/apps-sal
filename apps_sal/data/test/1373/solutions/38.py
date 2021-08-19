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
sys.setrecursionlimit(10 ** 7)


def cmb(n, r, mod):
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
        bunshi = bunshi * (n - i) % mod
    return bunshi * pow(bunbo, mod - 2, mod) % mod


mod = 10 ** 9 + 7


def I():
    return int(input())


def LI():
    return list(map(int, input().split()))


def MI():
    return list(map(int, input().split()))


def LLI(n):
    return [list(map(int, input().split())) for _ in range(n)]


(n, k) = MI()
ans = 0
for i in range(k, n + 2):
    ans += i * (n - i + 1) % mod + 1
print(ans % mod)
