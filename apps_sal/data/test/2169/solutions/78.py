import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
INF = float('inf')


def I():
    return int(input())


def F():
    return float(input())


def SS():
    return input()


def LI():
    return [int(x) for x in input().split()]


def LI_():
    return [int(x) - 1 for x in input().split()]


def LF():
    return [float(x) for x in input().split()]


def LSS():
    return input().split()


def resolve():
    (H, W, D) = LI()
    A = [LI_() for _ in range(H)]
    Q = I()
    c = [[] for _ in range(H * W)]
    for (i, j) in itertools.product(list(range(H)), list(range(W))):
        c[A[i][j]] = [i, j]
    c_cum = [0] * (H * W)
    for i in range(H * W - D):
        c_cum[i + D] = abs(c[i + D][0] - c[i][0]) + abs(c[i + D][1] - c[i][1]) + c_cum[i]
    for _ in range(Q):
        (L, R) = LI_()
        ans = c_cum[R] - c_cum[L]
        print(ans)


def __starting_point():
    resolve()


__starting_point()
