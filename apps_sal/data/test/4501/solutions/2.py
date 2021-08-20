import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('Yes') if fl else print('No')


def ncr(n, r):
    ret = 1
    if n < r:
        return 0
    if n - r < r:
        r = n - r
    for i in range(1, r + 1):
        ret *= n - r + i
        ret //= i
    return ret


(n, a) = ma()
X = lma()
for i in range(n):
    X[i] -= a
co = collections.Counter(X)
ans = 0
mx = 49 * n
dp = [[0 for j in range(-mx, mx + 1)] for i in range(n + 1)]
dp[-1][0] = 1
for i in range(n):
    x = X[i]
    for j in range(-mx, mx + 1, 1):
        dp[i][j] += dp[i - 1][j] + dp[i - 1][j - x]
print(dp[n - 1][0] - 1)
