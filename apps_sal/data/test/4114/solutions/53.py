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
    N = I()

    xyh_0 = []
    xyh_not0 = []
    for _ in range(N):
        xyh = LI()
        if xyh[2] == 0:
            xyh_0.append(xyh)
        else:
            xyh_not0.append(xyh)

    for cx, cy in itertools.product(list(range(101)), list(range(101))):
        H = []
        for x, y, h in xyh_not0:
            H.append(h + abs(x - cx) + abs(y - cy))
        if len(set(H)) == 1:
            is_ok = True
            for x, y, h in xyh_0:
                if max(H[0] - abs(x - cx) - abs(y - cy), 0) != 0:
                    is_ok = False
            if is_ok:
                ans = (cx, cy, H[0])

    print((*ans))


def __starting_point():
    resolve()


__starting_point()
