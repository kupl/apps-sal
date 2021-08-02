from collections import Counter
from collections import deque, defaultdict
import itertools as it
from math import gcd, floor, ceil, factorial
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


def inp():
    return int(input())


def inps():
    return input().rstrip()


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(map(str, input().split()))

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10


# from heapq import heappush, heappop, heapify
# import math


def lcd(a, b):
    return a * b // gcd(a, b)


def chmin(dp, i, x):
    if x < dp[i]: dp[i] = x; return True
    return False


def chmax(dp, i, x):
    if x > dp[i]: dp[i] = x; return True
    return False

# ---------------------------------------


a = inpl()
sm = sum(a)

if sm % 2 != 0:
    print("No")
    return

for b in range(2**len(a)):
    s = 0
    for i in range(len(a)):
        if 1 & b >> i:
            s += a[i]
    if s == sm // 2:
        print("Yes")
        return

print("No")
