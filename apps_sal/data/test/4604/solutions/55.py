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
MOD = 10 ** 9 + 7


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
    A = LI()
    if N % 2 == 0:
        if sorted(A) == [i // 2 * 2 + 1 for i in range(N)]:
            print(pow(2, N // 2, MOD))
        else:
            print(0)
    elif sorted(A) == [(i // 2 + 1) * 2 for i in range(-1, N - 1)]:
        print(pow(2, (N - 1) // 2, MOD))
    else:
        print(0)


def __starting_point():
    resolve()


__starting_point()
