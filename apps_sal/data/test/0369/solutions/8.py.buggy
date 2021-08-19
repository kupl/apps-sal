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


def solve():
    N, M = Scanner.map_int()
    S = Scanner.string()
    pos = N
    ans = []
    while pos > 0:
        for i in range(max(pos - M, 0), pos):
            if S[i] == '0':
                ans.append(pos - i)
                pos = i
                break
        else:
            print((-1))
            return
    print((*ans[::-1]))


def main():
    # sys.setrecursionlimit(1000000)
    # sys.stdin = open("sample.txt")
    solve()


def __starting_point():
    main()


__starting_point()
