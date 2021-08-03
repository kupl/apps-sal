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
    N, K = LI()
    S = SS()

    # 1の塊の長さと位置を調べる
    l = []
    if S[0] == '1':
        l.append(0)
    # 先端0の場合、一番左に長さ0の1の塊があるとする
    else:
        l.append(0)
        l.append(0)
    for i in range(N - 1):
        if S[i] == '0' and S[i + 1] == '1':
            l.append(i + 1)
        elif S[i] == '1' and S[i + 1] == '0':
            l.append(i + 1)
    if S[-1] == '1':
        l.append(N)
    # 後端0の場合、一番右に長さ0の1の塊があるとする
    else:
        l.append(N)
        l.append(N)

    ans = 0
    # 0の塊がK個以下の場合
    if len(l) // 2 - 1 < K:
        ans = N
    # 1の塊をK+1個くっつけた場合の長さを調べる
    else:
        for i in range(len(l) // 2 - K):
            ans = max(l[2 * i + 2 * K + 1] - l[2 * i], ans)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
