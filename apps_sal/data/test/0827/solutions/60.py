#!/usr/bin/env python3
# from typing import *

import io
import sys
import math
import collections
import decimal
import itertools

sys.setrecursionlimit(1000000)

# _INPUT = """2
# 01
# """
# sys.stdin = io.StringIO(_INPUT)


def is_T_ok(T):
    if T[0] == 0:
        k = 0
    elif T[1] == 0:
        k = 1
    elif T[2] == 0:
        k = 2
    else:
        return False

    for i in range(len(T)):
        if i % 3 == k:
            if T[i] != 0:
                return False
        else:
            if T[i] != 1:
                return False

    return True


def solve(N, T):

    if T == [0]:
        return 10**10
    elif T == [1]:
        return 10**10 * 2
    elif T == [1, 1]:
        return 10**10

    if not is_T_ok(T):
        return 0

    count0 = T.count(0)
    if T[-1] == 0:
        return 10**10 - count0 + 1
    else:
        return 10**10 - count0


def main():
    N = int(input())
    T = list(map(int, input()))
    a = solve(N, T)
    print(a)


def __starting_point():
    main()


__starting_point()
