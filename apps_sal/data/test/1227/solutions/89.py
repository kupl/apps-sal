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


def solve():
    S = Scanner.string()
    N = len(S)
    K = Scanner.int()
    dp = [[[0 for _ in range(2)] for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(2):
                nd = int(S[i])
                for d in range(10):
                    ni, nj, nk = i + 1, j, k
                    if d != 0:
                        nj += 1
                    if nj > K:
                        continue
                    if k == 0:
                        if d > nd:
                            continue
                        if d < nd:
                            nk += 1
                    dp[ni][nj][nk] += dp[i][j][k]
    print((dp[N][K][0] + dp[N][K][1]))


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
