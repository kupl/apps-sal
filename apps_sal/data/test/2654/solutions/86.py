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


MOD = int(1000000000.0) + 7
INF = int(1000000000000000.0)


def solve():
    N = Scanner.int()
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        (A[i], B[i]) = Scanner.map_int()
    A.sort()
    B.sort()
    if N % 2 == 0:
        mA = A[N // 2] + A[N // 2 - 1]
        mB = B[N // 2] + B[N // 2 - 1]
        print(mB - mA + 1)
    else:
        mA = A[N // 2]
        mB = B[N // 2]
        print(mB - mA + 1)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
