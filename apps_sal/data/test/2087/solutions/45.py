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


mod = 998244353


def I():
    return int(input())


def LI():
    return list(map(int, input().split()))


def MI():
    return list(map(int, input().split()))


def LLI(n):
    return [list(map(int, input().split())) for _ in range(n)]


(a, b, c) = MI()
sum_a = a * (a + 1) // 2
sum_b = b * (b + 1) // 2
sum_c = c * (c + 1) // 2
sum_a = sum_a % mod
sum_b = sum_b % mod
sum_c = sum_c % mod
print(sum_a * sum_b * sum_c % mod)
