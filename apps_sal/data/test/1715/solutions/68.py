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
    A, B, Q = LI()
    s = [I() for _ in range(A)]
    t = [I() for _ in range(B)]

    # xから一番近い神社に行く→その神社から一番近い寺に行く、またはその逆の2パターン

    # 各神社に対する一番近い寺の距離を求めておく
    len_of_nearest_t = [INF] * A
    for i in range(A):
        idx = bisect.bisect_left(t, s[i])
        len_r = t[idx] - s[i] if 0 <= idx < B else INF
        len_l = s[i] - t[idx - 1] if 0 <= idx - 1 < B else INF
        len_of_nearest_t[i] = min(len_l, len_r)
    # print(len_of_nearest_t)

    # 各寺に対する一番近い神社の距離を求めておく
    len_of_nearest_s = [INF] * B
    for i in range(B):
        idx = bisect.bisect_left(s, t[i])
        len_r = s[idx] - t[i] if 0 <= idx < A else INF
        len_l = t[i] - s[idx - 1] if 0 <= idx - 1 < A else INF
        len_of_nearest_s[i] = min(len_l, len_r)
    # print(len_of_nearest_s)

    for _ in range(Q):
        x = I()
        # 神社→寺
        idx = bisect.bisect_left(s, x)
        len_r = s[idx] - x + len_of_nearest_t[idx] if 0 <= idx < A else INF
        len_l = x - s[idx - 1] + len_of_nearest_t[idx - 1] if 0 <= idx - 1 < A else INF
        len_x_s_t = min(len_r, len_l)
        # 寺→神社
        idx = bisect.bisect_left(t, x)
        len_r = t[idx] - x + len_of_nearest_s[idx] if 0 <= idx < B else INF
        len_l = x - t[idx - 1] + len_of_nearest_s[idx - 1] if 0 <= idx - 1 < B else INF
        len_x_t_s = min(len_r, len_l)
        print((min(len_x_s_t, len_x_t_s)))


def __starting_point():
    resolve()


__starting_point()
