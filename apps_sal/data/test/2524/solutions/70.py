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


class Math:

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Math.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return a * b // Math.gcd(a, b)

    @staticmethod
    def divisor(n):
        res = []
        i = 1
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
        return res

    @staticmethod
    def round_up(a, b):
        return -(-a // b)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3, d + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
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


def pop_count(x):
    x = x - (x >> 1 & 6148914691236517205)
    x = (x & 3689348814741910323) + (x >> 2 & 3689348814741910323)
    x = x + (x >> 4) & 1085102592571150095
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 127


MOD = int(1000000000.0) + 7
INF = int(1000000000000000.0)


def solve():
    N = Scanner.int()
    A = Scanner.map_int()
    ans = 0
    for i in range(61):
        p = 1
        for _ in range(i):
            p *= 2
            p %= MOD
        x = 0
        for a in A:
            if a >> i & 1:
                x += 1
        t = x * (N - x)
        t %= MOD
        t *= p
        t %= MOD
        ans += t
        ans %= MOD
    print(ans)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
