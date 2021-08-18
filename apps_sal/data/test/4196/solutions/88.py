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
    A = LI()

    gcd_cum_l = [0] * (N + 1)
    for i in range(N):
        gcd_cum_l[i + 1] = math.gcd(A[i], gcd_cum_l[i])
    gcd_cum_r = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        gcd_cum_r[i] = math.gcd(A[i], gcd_cum_r[i + 1])

    ans = 0
    for i in range(N):
        ans = max(math.gcd(gcd_cum_l[i], gcd_cum_r[i + 1]), ans)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
