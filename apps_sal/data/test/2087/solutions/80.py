
import sys
import io
import math
import collections
import decimal
import itertools
from queue import PriorityQueue
import bisect


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)


MOD = 998244353


def solve(A, B, C):
    pass


def main():
    A, B, C = list(map(int, input().split()))
    a = (A * (A + 1) // 2) * (B * (B + 1) // 2) * (C * (C + 1) // 2)
    print((a % MOD))


def __starting_point():
    main()


__starting_point()
