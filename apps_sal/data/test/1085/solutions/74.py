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


MOD = 998244353
INF = int(1000000000000000.0)


def divisor(N):
    res = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            res.append(i)
            if i != N // i:
                res.append(N // i)
        i += 1
    if N != 1:
        res.append(N)
    return res


def solve():
    N = Scanner.int()
    d0 = divisor(N - 1)
    ans = len(d0)
    d1 = divisor(N)
    for d in d1:
        X = N
        while X % d == 0:
            X //= d
        if X % d == 1:
            ans += 1
    print(ans)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
