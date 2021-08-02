import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
input = lambda: sys.stdin.readline().rstrip()
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
    N = I()
    A = LI()
    B = LI()

    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] -= min(A[i], B[i])
        ans += min(A[i + 1], B[i])
        A[i + 1] -= min(A[i + 1], B[i])

    print(ans)


def __starting_point():
    resolve()


__starting_point()
