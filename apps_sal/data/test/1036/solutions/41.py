import sys
import math
import random
import re
import heapq
from itertools import combinations as c, permutations as perm, product as p
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**9)
INF = float('inf')
#MOD = 10**9 + 7
MOD = 998244353
F = 1e-9


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lintdec(): return list(map(lambda x: int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [ii() for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]
def lcm(a, b): return a * b // math.gcd(a, b)


#######################################################
N, K = lint()
S = si()
J = {'R': 0, 'S': 1, 'P': 2}
dp = [[0] * 110 for _ in range(110)]


def winner(x, y):
    if (J[x] - J[y] + 3) % 3 == 1:
        return y
    return x


def tournament(m, n):
    if n == 0:
        dp[m][n] = S[m]
    if dp[m][n]:
        return dp[m][n]

    a = tournament(m, n - 1)
    b = tournament((m + pow(2, n - 1, N)) % N, n - 1)
    dp[m][n] = winner(a, b)
    return dp[m][n]


def main():
    print(tournament(0, K))


def __starting_point():
    main()


__starting_point()
