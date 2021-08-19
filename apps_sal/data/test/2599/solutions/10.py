# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right
from collections import deque
from collections import Counter
from itertools import accumulate, combinations, permutations
from heapq import heapify, heappop, heappush
from functools import lru_cache


def input(): return sys.stdin.readline()[:-1]
def printl(li): _ = print(*li, sep="\n") if li else None


def argsort(s, return_sorted=False):
    inds = sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted:
        return inds, [s[i] for i in inds]
    return inds


def alp2num(c, cap=False): return ord(c) - 97 if not cap else ord(c) - 65
def num2alp(i, cap=False): return chr(i + 97) if not cap else chr(i + 65)


def matmat(A, B):
    K, N, M = len(B), len(A), len(B[0])
    return [[sum([(A[i][k] * B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]


def matvec(M, v):
    N, size = len(v), len(M)
    return [sum([M[i][j] * v[j] for j in range(N)]) for i in range(size)]


def T(M):
    n, m = len(M), len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]


def main():
    mod = 1000000007
    # w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, K = map(int, input().split())
    # A = tuple(map(int, input().split())) #1行ベクトル
    # L = tuple(int(input()) for i in range(N)) #改行ベクトル
    # S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    n, k = N, K
    ans = float('inf')

    def f(tot, ini, j, kuri):
        r = ini
        # if r>tot:
        #    return -1

        i = 0
        for ji in range(j):
            i += 1
            r += 10**i * 9

        c = 0
        while tot > 0:
            i += 1
            if c == 0 and kuri:
                nex = min(tot, 8)
            else:
                nex = min(tot, 9)
            tot -= nex
            r += nex * 10**i
            c += 1
        return r

    trs = n // 9

    for j in range(0, trs + 2):
        for ini in range(0, 10):
            kuri = 0
            ctot = 9 * j + ini

            for i in range(1, k + 1):
                ad = ini + i
                if ad < 10:
                    ctot += 9 * j + ad
                else:
                    kuri = 1
                    ctot += 1 + ad % 10

            ktot = n - ctot
            if ktot < 0 or ktot % (k + 1) != 0:
                continue
            tot = ktot // (k + 1)
            ans = min(ans, f(tot, ini, j, kuri))

    if ans != float("inf"):
        print(ans)
    else:
        print(-1)


def __starting_point():
    q = int(input())
    for _ in range(q):
        main()


__starting_point()
