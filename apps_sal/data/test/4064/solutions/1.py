#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n, h, l, r = map(int, input().split())
a = [int(item) for item in input().split()]
dp = [[-1] * h for _ in range(n + 1)]
dp[0][0] = 0

for i, item in enumerate(a):
    for j in range(h):
        if dp[i][j] == -1:
            continue
        # Sleep early
        nt = (j + item) % h
        if l <= nt <= r:
            dp[i + 1][nt] = max(dp[i + 1][nt], dp[i][j] + 1)
        else:
            dp[i + 1][nt] = max(dp[i + 1][nt], dp[i][j])
        # Sleep normaly
        nt = (j + item - 1 + h) % h
        if l <= nt <= r:
            dp[i + 1][nt] = max(dp[i + 1][nt], dp[i][j] + 1)
        else:
            dp[i + 1][nt] = max(dp[i + 1][nt], dp[i][j])
print(max(dp[-1]))
