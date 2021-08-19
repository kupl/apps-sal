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
    (N, K) = LI()
    num_0 = N // K
    if K % 2 == 0:
        num_K_half = N // K + (1 if N % K >= K // 2 else 0)
    else:
        num_K_half = 0
    ans = num_0 ** 3 + num_K_half ** 3
    print(ans)


def __starting_point():
    resolve()


__starting_point()
