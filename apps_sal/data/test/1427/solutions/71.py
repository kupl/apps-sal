# -*- coding: utf-8 -*-
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


def pop_count(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


MOD = 10**9 + 7


def fact(N):
    res = {}
    tmp = N
    for i in range(2, int(N ** 0.5 + 1) + 1):
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp //= i
        if cnt > 0:
            res[i] = cnt
    if tmp != 1:
        res[tmp] = 1
    if res == {}:
        res[N] = 1
    return res


def modpow(n, p):
    res = 1
    while p > 0:
        if p & 1:
            res = res * n % MOD
        n = n * n % MOD
        p >>= 1
    return res


def modinv(n):
    b, u, v = MOD, 1, 0
    while b > 0:
        t = n // b
        n -= t * b
        n, b = b, n
        u -= t * v
        u, v = v, u
    u %= MOD
    if u < 0:
        u += MOD
    return u


def solve():
    N = Scanner.int()
    A = Scanner.map_int()
    L = defaultdict(int)
    for i in range(N):
        for k, v in list(fact(A[i]).items()):
            L[k] = max(L[k], v)
    lcm = 1
    for k, v in list(L.items()):
        lcm *= modpow(k, v)
        lcm %= MOD
    ans = 0
    for i in range(N):
        x = lcm * modinv(A[i]) % MOD
        ans += x
        ans %= MOD
    print(ans)


def main():
    # sys.setrecursionlimit(1000000)
    # sys.stdin = open("sample.txt")
    # T = Scanner.int()
    # for _ in range(T):
    #     solve()
    # print('YNeos'[not solve()::2])
    solve()


def __starting_point():
    main()


__starting_point()
