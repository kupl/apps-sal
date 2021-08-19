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
    (N, C) = LI()
    D = [LI() for _ in range(C)]
    c = [LI_() for _ in range(N)]
    a = [[0] * C for _ in range(3)]
    for (i, j) in itertools.product(list(range(N)), repeat=2):
        for k in range(C):
            a[(i + j) % 3][k] += D[c[i][j]][k]
    ans = INF
    for (i, j, k) in itertools.permutations(list(range(C)), 3):
        ans = min(a[0][i] + a[1][j] + a[2][k], ans)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
