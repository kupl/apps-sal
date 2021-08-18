from collections import Counter
from collections import deque, defaultdict
import itertools as it
from math import gcd, floor, ceil, factorial
import sys
input = sys.stdin.readline


def inp():
    return int(input())


def inps():
    return input().rstrip()


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(map(str, input().split()))


def lcd(a, b):
    return a * b // gcd(a, b)


def chmin(dp, i, x):
    if x < dp[i]:
        dp[i] = x
        return True
    return False


def chmax(dp, i, x):
    if x > dp[i]:
        dp[i] = x
        return True
    return False


N, K = inpl()
mn = 1 * 2
mx = N * 2
mid = (mx - mn) // 2 + mn

dp = [0] * (mx + 1)
for i in range(mn, mx + 1):
    dp[i] = mid - abs(i - mid) - 1

ans = 0
for i in range(mn, mx + 1):
    j = i - K
    if mn <= j <= mx:
        ans += dp[i] * dp[j]

print(ans)
