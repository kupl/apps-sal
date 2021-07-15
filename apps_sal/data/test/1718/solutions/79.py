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
from math import gcd, floor, ceil, factorial
import itertools as it
from collections import deque, defaultdict
from collections import Counter

def lcd(a, b):
    return a * b // gcd(a, b)

def chmin(dp, i, x):
    if x < dp[i]: dp[i] = x; return True
    return False

def chmax(dp, i, x): 
    if x > dp[i]: dp[i] = x; return True
    return False

# ---------------------------------------

N, K = inpl()
A = inpl()

if N == K:
    print((1))
    return

idx = 0
for i in range(N):
    if A[i] == 1:
        idx = i
        break

left = N - i
right = N - left - 1

start = max(0, (K - 1) - right)
end = max(K - 1, left)
ans = 10 ** 10
for i in range(start, end + 1):
    l = left - i
    r = right - (K - 1 - i)
    if l == 0:
        l = 0
    else:
        l = (l - 0.5) // (K - 1) + 1
    if r == 0:
        r = 0
    else:
        r = (r - 0.5) // (K - 1) + 1
    ans = min(ans, int(l + r + 1))
print(ans)

