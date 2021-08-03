import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


cnt = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n, m = ma()
A = lma()
use = [(cnt[a], a) for a in A]
use.sort(key=lambda x: x[1], reverse=True)
INF = 10**9
dp = [0] + [-INF] * (n + 10)
for i in range(n):
    if dp[i] == -INF:
        continue
    for c, a in use:
        dp[i + c] = max(dp[i + c], dp[i] + 1)
l = dp[n]
ans = ["0"] * l
num = n
for i in range(l):
    for c, a in use:
        if dp[num - c] == dp[num] - 1:
            ans[i] = str(a)
            num -= c
            break
print("".join(ans))
