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


def solve():
    H, W, K = Scanner.map_int()
    S = Scanner.string_list(H)
    ans = int(1e15)
    for i in range(1 << (H - 1)):
        cut = 0
        pc = 1
        whites = [[0 for _ in range(W)] for _ in range(H)]
        for j in range(H - 1):
            for w in range(W):
                whites[cut][w] += S[j][w] == '1'
            if i >> j & 1:
                cut += 1
                pc += 1
        for w in range(W):
            whites[cut][w] += S[-1][w] == '1'
        flag = True
        for line in whites:
            for cnt in line:
                if cnt > K:
                    flag = False
        if not flag:
            continue
        cnt = [0 for _ in range(pc)]
        for w in range(W):
            flag = True
            for j in range(pc):
                if cnt[j] + whites[j][w] > K:
                    flag = False
            if not flag:
                cnt = [0 for _ in range(pc)]
                cut += 1
            for j in range(pc):
                cnt[j] += whites[j][w]
        ans = min(ans, cut)
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
