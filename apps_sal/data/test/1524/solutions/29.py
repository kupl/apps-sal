import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


ans = [0] * 101010
S = ns()
dp = [[0 for i in range(101010)] for j in range(34)]
N = len(S)
for i in range(N):
    dp[0][i] = i - 1 if S[i] == 'L' else i + 1
for p in range(33):
    for i in range(N):
        dp[p + 1][i] = dp[p][dp[p][i]]
for i in range(N):
    ans[dp[32][i]] += 1
print(*ans[:N])
