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
    N, K = LI()
    S = SS()

    # 1の塊の長さと位置を調べる
    l = []
    if S[0] == '1':
        l.append(0)
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
    else:
        l.append(N)
        l.append(N)
    # print(S)
    # print(l)

    # 1の塊をK+1個くっつけた場合の長さを調べる
    ans = 0
    if len(l) // 2 - 1 < K:
        ans = N
    else:
        for i in range(len(l) // 2 - K):
            ans = max(l[2 * i + 2 * K + 1] - l[2 * i], ans)

    # 端の0を逆立ちさせた場合
    # if S[0] == '0':
    #     ans = max(l[2*K-1], ans)
    # if S[-1] == '0':
    #     ans = max(N - l[len(l)-2*K], ans)

    # 全部1だった場合(塊の間も無いし端の0もない)
    # if l == [0, N]:
    #     ans = N

    print(ans)


def __starting_point():
    resolve()


__starting_point()
