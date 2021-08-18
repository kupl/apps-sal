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
    AB = [LI() for _ in range(N)]

    W = [[] for _ in range(M + 1)]
    for a, b in AB:
        if 0 <= M - a:
            W[M - a].append(b)

    ans = 0
    hq = []
    for i in reversed(W):
        for j in i:
            heapq.heappush(hq, -j)
        if hq:
            ans -= heapq.heappop(hq)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
