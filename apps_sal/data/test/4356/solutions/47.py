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
    N, M = LI()
    A = [SS() for _ in range(N)]
    B = [SS() for _ in range(M)]

    is_ok = False
    for i, j in itertools.product(list(range(N - M + 1)), repeat=2):
        tmp = True
        for k in range(M):
            if B[k] != A[i + k][j:j + M]:
                tmp = False
                break
        if tmp:
            is_ok = True
            break

    if is_ok:
        print('Yes')
    else:
        print('No')


def __starting_point():
    resolve()


__starting_point()
