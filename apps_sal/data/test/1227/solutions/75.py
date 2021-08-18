import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


def main():
    s = S()
    n = len(s)
    K = I()

    dp = [[[0] * 2 for _ in range(4)] for __ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        nd = int(s[i])
        for j in range(4):
            for k in range(2):
                for d in range(10):
                    ni = i + 1
                    nj = j
                    nk = k

                    if d != 0:
                        nj += 1

                    if K < nj:
                        continue

                    if nk == 0:
                        if d < nd:
                            nk = 1
                        if nd < d:
                            continue

                    dp[ni][nj][nk] += dp[i][j][k]

    return dp[n][K][0] + dp[n][K][1]


print((main()))
