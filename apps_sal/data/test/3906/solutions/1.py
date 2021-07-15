3

import array
import math
import os
import sys


MOD = 10 ** 9 + 7


def main():
    N, M = read_ints()
    print(solve(N, M))


def solve(N, M):
    def row_count(w):
        dp = [0] * (w + 1)
        dp[0] = 1
        for i in range(w):
            if i + 1 <= w:
                dp[i + 1] += dp[i]
                dp[i + 1] %= MOD
            if i + 2 <= w:
                dp[i + 2] += dp[i]
                dp[i + 2] %= MOD
        return dp[w]

    c = row_count(N)
    r = row_count(M)

    return ((c + r - 1) * 2) % MOD


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()

__starting_point()
