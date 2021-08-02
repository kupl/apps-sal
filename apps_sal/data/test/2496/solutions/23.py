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


def primeFactorization(n):
    D = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if D[i] == i:
            for j in range(i, n + 1, i):
                if D[j] == j:
                    D[j] = i
    return D


def resolve():
    N = I()
    A = LI()

    # pairwise判定
    is_pc = True
    D = primeFactorization(max(A))
    pf = set()
    for i in A:
        tmp = i
        cnt = collections.Counter()
        while tmp != 1:
            cnt[D[tmp]] += 1
            tmp //= D[tmp]
        fact = set(cnt.keys())
        if pf & fact:
            is_pc = False
            break
        else:
            pf |= fact

    # setwise判定
    is_sc = False
    if not is_pc:
        gcd = A[0]
        for i in A[1:]:
            gcd = math.gcd(i, gcd)
        if gcd == 1:
            is_sc = True

    if is_pc:
        print('pairwise coprime')
    elif is_sc:
        print('setwise coprime')
    else:
        print('not coprime')


def __starting_point():
    resolve()


__starting_point()
