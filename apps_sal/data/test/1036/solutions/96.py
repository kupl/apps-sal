from sys import stdin, setrecursionlimit
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 1000000007


def input():
    return stdin.readline().strip()


def main():
    (n, k) = list(map(int, input().split()))
    s = input()
    dp = [['' for _ in range(105)] for _ in range(105)]
    for i in range(n):
        dp[0][i] = s[i]
    for i in range(1, k + 1):
        for j in range(n):
            a = dp[i - 1][j]
            b = dp[i - 1][(j + pow(2, i - 1)) % n]
            st = {a, b}
            rec = ''
            if st == set('RS'):
                rec = 'R'
            elif st == set('SP'):
                rec = 'S'
            elif st == set('PR'):
                rec = 'P'
            else:
                rec = a
            dp[i][j] = rec
    ans = dp[k][0]
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
