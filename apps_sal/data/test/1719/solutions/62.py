import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 10**9 + 7

N = int(input())
memo = [{} for _ in range(N + 1)]


def ok(last4):
    for i in range(4):
        t = list(last4)
        if i > 0:
            t[i - 1], t[i] = t[i], t[i - 1]
        if 'AGC' in ''.join(t):
            return 0
    return 1


def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    res = 0
    for c in 'AGCT':
        if ok(last3 + c):
            res = (res + dfs(cur + 1, last3[1:] + c)) % m
    memo[cur][last3] = res
    return res


print(dfs(0, 'TTT'))
