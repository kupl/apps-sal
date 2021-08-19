#!/usr/bin/env python3
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

# bisect.bisect_left(list,key)はlistのなかでkey未満の数字がいくつあるかを返す
# つまりlist[i] < x となる i の個数
# bisect.bisect_right(list, key)はlistのなかでkey以下の数字がいくつあるかを返す
# つまりlist[i] <= x となる i の個数
# これを応用することで
# len(list) - bisect.bisect_left(list,key)はlistのなかでkey以上の数字がいくつあるかを返す
# len(list) - bisect.bisect_right(list,key)はlistのなかでkeyより大きい数字がいくつあるかを返す
# これらを使うときはあらかじめlistをソートしておくこと！


def func(n, k):
    return min(k - 1, 2 * n + 1 - k)


n, k = MI()
A = max(2, 2 + k)
B = min(2 * n, 2 * n + k)
ans = 0
for x in range(A, B + 1):
    ans += func(n, x) * func(n, x - k)
print(ans)
