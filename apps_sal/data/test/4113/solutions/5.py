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
    N = I()
    is_ok = False
    for i in range(N // 7 + 1):
        if (N - 7 * i) % 4 == 0:
            is_ok = True
    if is_ok:
        print('Yes')
    else:
        print('No')


def __starting_point():
    resolve()


__starting_point()
