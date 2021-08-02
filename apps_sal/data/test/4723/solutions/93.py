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
    S_ = SS()
    T = SS()

    len_S = len(S_)
    len_T = len(T)

    # TはS'のなるべく右側にあるべき
    idx = -1
    for i in range(len_S - len_T, -1, -1):
        exists = True
        for j in range(len_T):
            if S_[i + j] != '?' and S_[i + j] != T[j]:
                exists = False
                break
        if exists:
            idx = i
            break

    if idx == -1:
        print('UNRESTORABLE')
    else:
        ans = list(S_)
        for i in range(len_S):
            if S_[i] == '?':
                if idx <= i < idx + len_T:
                    ans[i] = T[i - idx]
                else:
                    ans[i] = 'a'

        print((''.join(ans)))


def __starting_point():
    resolve()


__starting_point()
