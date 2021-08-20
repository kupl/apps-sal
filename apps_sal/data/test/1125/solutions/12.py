from itertools import accumulate, combinations, permutations
from heapq import heapify, heappop, heappush
from functools import lru_cache
from collections import Counter
from bisect import bisect_left, bisect, bisect_right
from decimal import Decimal
from collections import deque
from operator import itemgetter
from copy import deepcopy as dcp
from copy import copy, deepcopy
import math
import sys
sys.setrecursionlimit(10 ** 7)


def input():
    x = sys.stdin.readline()
    return x[:-1] if x[-1] == '\n' else x


def printl(li):
    _ = print(*li, sep='\n') if li else None


def argsort(s, return_sorted=False):
    inds = sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted:
        return (inds, [s[i] for i in inds])
    return inds


def alp2num(c, cap=False):
    return ord(c) - 97 if not cap else ord(c) - 65


def num2alp(i, cap=False):
    return chr(i + 97) if not cap else chr(i + 65)


def matmat(A, B):
    (K, N, M) = (len(B), len(A), len(B[0]))
    return [[sum([A[i][k] * B[k][j] for k in range(K)]) for j in range(M)] for i in range(N)]


def matvec(M, v):
    (N, size) = (len(v), len(M))
    return [sum([M[i][j] * v[j] for j in range(N)]) for i in range(size)]


def T(M):
    (n, m) = (len(M), len(M[0]))
    return [[M[j][i] for j in range(n)] for i in range(m)]


def main():
    mod = 1000000007
    N = int(input())
    A = tuple(map(int, input().split()))
    ref = 0
    for i in range(2, N):
        ref ^= A[i]
    a0 = A[0]
    a1 = A[1]
    ans = 0
    INF = 10 ** 13

    @lru_cache(None)
    def dfs(a0, a1, ref):
        inf = INF
        if a0 & 1 ^ a1 & 1 != ref & 1:
            return inf
        if a0 < 0:
            return inf
        if ref == 0:
            return inf if a0 < a1 else (a0 - a1) // 2
        a01 = a0 & 1
        a11 = a1 & 1
        ref1 = ref & 1
        ans = inf
        if a01 ^ a11 == ref1:
            ans = min(ans, 2 * dfs(a0 >> 1, a1 >> 1, ref >> 1))
        ans = min(ans, 2 * dfs((a0 - 1) // 2, (a1 + 1) // 2, ref >> 1) + 1)
        return ans
    x = dfs(a0, a1, ref)
    if x >= a0:
        print(-1)
    else:
        print(x)


def __starting_point():
    main()


__starting_point()
