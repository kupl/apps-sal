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
import decimal


class Scanner():
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


MOD = 998244353
INF = int(1e15)


def solve():
    MAX = 200010
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    N, M, K = Scanner.map_int()
    ans = 0
    for k in range(K + 1):
        tmp = M * pow(M - 1, N - 1 - k, MOD)
        tmp %= MOD
        cmb = fac[N - 1] * (finv[k] * finv[N - 1 - k] % MOD) % MOD
        tmp *= cmb
        tmp %= MOD
        ans += tmp
        ans %= MOD
    print(ans)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
