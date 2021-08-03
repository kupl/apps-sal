import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N, x = LI()
    a = LI()

    # 隣り合う2つの和
    s = [a[i] + a[i + 1] for i in range(N - 1)]
    # 隣り合う2つの和をx以下にしたもの
    s_after = [min(i, x) for i in s]

    # 隣り合う2つの和をx以下にしたものから元の数列を復元
    a_after = [0] * N
    a_after[0] = min(a[0], s_after[0])
    for i in range(N - 1):
        a_after[i + 1] = min(s_after[i] - a_after[i], a[i + 1])

    ans = sum(a) - sum(a_after)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
