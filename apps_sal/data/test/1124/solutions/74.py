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


N = inp()
a = inpl()

for i in range(len(a)):
    if i == 0:
        ans = a[i]
    else:
        ans = gcd(ans, a[i])
print(ans)
