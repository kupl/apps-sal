from math import floor, ceil, pi, factorial
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, accumulate, groupby, product
from collections import defaultdict
from collections import Counter, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print(('\n'.join(x)))
def printni(x): print(('\n'.join(list(map(str, x)))))


inf = 10**17
mod = 10**9 + 7

h, w, k = MI()
dp = [[0] * w for i in range(h + 1)]
dp[0][0] = 1
a = 0
b = 1
weight = []
for i in range(100):
    weight.append(a + b)
    a, b = b, a + b
for i in range(h):
    for j in range(w):
        if 0 <= j + 1 < w:
            left = max(j - 1, 0)
            right = max(w - j - 3, 0)
            dp[i + 1][j + 1] += (dp[i][j] * weight[left] * weight[right]) % mod
        if 0 <= j < w:
            left = max(j - 1, 0)
            right = max(w - j - 2, 0)
            dp[i + 1][j] += (dp[i][j] * weight[left] * weight[right]) % mod
        if 0 <= j - 1 < w:
            left = max(j - 2, 0)
            right = max(w - j - 2, 0)
            dp[i + 1][j - 1] += (dp[i][j] * weight[left] * weight[right]) % mod
print((dp[-1][k - 1] % mod))
