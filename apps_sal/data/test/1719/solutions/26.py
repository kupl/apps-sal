import random
import time
from itertools import permutations
from operator import itemgetter
from collections import deque
from collections import Counter
import math
import sys
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7


def dfs(s):
    if len(s) == N:
        return 1
    if s[-2] == 'A' and s[-1] == 'G' or (s[-2] == 'G' and s[-1] == 'A'):
        return dfs(s + 'A') % MOD + dfs(s + 'G') % MOD + dfs(s + 'T') % MOD
    elif s[-2] == 'A' and s[-1] == 'C':
        return dfs(s + 'A') % MOD + dfs(s + 'C') % MOD + dfs(s + 'T') % MOD
    else:
        return dfs(s + 'A') % MOD + dfs(s + 'C') % MOD + dfs(s + 'G') % MOD + dfs(s + 'T') % MOD


def main():
    N = int(readline())
    (A, G, C, T) = (0, 1, 2, 3)
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == A and k == G and (l == C):
                    continue
                if j == A and k == C and (l == G):
                    continue
                if j == G and k == A and (l == C):
                    continue
                dp[3][j][k][l] = 1
    for i in range(4, N + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == A and k == G and (l == C):
                            continue
                        if j == A and k == C and (l == G):
                            continue
                        if j == G and k == A and (l == C):
                            continue
                        if m == A and k == G and (l == C):
                            continue
                        if m == A and j == G and (l == C):
                            continue
                        dp[i][j][k][l] += dp[i - 1][m][j][k]
                        dp[i][j][k][l] %= MOD
    res = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                res += dp[N][j][k][l]
                res %= MOD
    print(res)


def __starting_point():
    main()


__starting_point()
