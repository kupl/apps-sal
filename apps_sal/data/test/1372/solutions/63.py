#!/usr/bin python3
# -*- coding: utf-8 -*-

h, n = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

# DP[i] = i までの魔法でモンスターの体力を減らすため消耗する魔力の最小値
dp = [0] * 20001

for i in range(h):
    dp[i] = min(dp[i - a] + b for a, b in ab)
print((dp[h - 1]))
