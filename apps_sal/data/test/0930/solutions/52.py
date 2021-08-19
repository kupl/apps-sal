import sys
import math
import os
import itertools
import string
import heapq
import _collections
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import lru_cache
import bisect
import re
import queue
import copy
import decimal


class Scanner:

    @staticmethod
    def int():
        return int(sys.stdin.readline().rstrip())

    @staticmethod
    def string():
        return sys.stdin.readline().rstrip()

    @staticmethod
    def map_int():
        return [int(x) for x in Scanner.string().split()]

    @staticmethod
    def string_list(n):
        return [Scanner.string() for i in range(n)]

    @staticmethod
    def int_list_list(n):
        return [Scanner.map_int() for i in range(n)]

    @staticmethod
    def int_cols_list(n):
        return [Scanner.int() for i in range(n)]


def pop_count(x):
    x = x - (x >> 1 & 6148914691236517205)
    x = (x & 3689348814741910323) + (x >> 2 & 3689348814741910323)
    x = x + (x >> 4) & 1085102592571150095
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 127


def solve():
    (N, K) = Scanner.map_int()
    MOD = int(1000000000.0) + 7
    MAX = 200010
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX
    fac[0] = fac[1] = finv[0] = finv[1] = inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    def cmb(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
    ans = 0
    for m in range(0, min(K, N - 1) + 1):
        a = cmb(N, m)
        b = cmb(N - 1, m)
        ans += a * b
        ans %= MOD
    print(ans)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
