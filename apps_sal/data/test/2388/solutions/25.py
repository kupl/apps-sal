#!/usr/bin/env python3
import sys
input = sys.stdin.readline
MOD = 998244353

n = int(input())
xd = []
# Add sentinel
places = [(10**12, 0)]
for _ in range(n):
    x, d = [int(item) for item in input().split()]
    xd.append((x, d))

xd.sort(reverse=True)
dp = [0] * (n + 1)
dp[0] = 1
for i, (x, d) in enumerate(xd):
    frm = x
    too = x + d
    too_idx = i
    while too > places[-1][0]:
        _, too_idx = places.pop()
    places.append((frm, too_idx))
    dp[i + 1] = dp[i] + dp[too_idx]
    dp[i + 1] %= MOD

print(dp[-1])
