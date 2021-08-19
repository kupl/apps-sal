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
MOD = 1000000007


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
    S = [SS() for _ in range(2)]
    t = []
    i = 0
    if N == 1:
        t.append('v')
    else:
        while i + 1 < N:
            if S[0][i] == S[0][i + 1]:
                t.append('h')
                i += 2
            else:
                t.append('v')
                i += 1
        if S[0][-2] != S[0][-1]:
            t.append('v')
    ans = 1
    if t[0] == 'h':
        ans *= 6
    else:
        ans *= 3
    ans %= MOD
    for i in range(len(t) - 1):
        if t[i] == 'h':
            if t[i + 1] == 'h':
                ans *= 3
            else:
                ans *= 1
        elif t[i + 1] == 'h':
            ans *= 2
        else:
            ans *= 2
        ans %= MOD
    print(ans)


def __starting_point():
    resolve()


__starting_point()
