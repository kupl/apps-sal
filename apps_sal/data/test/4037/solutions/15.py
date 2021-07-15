# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:12:02 2020

@author: Rodro
"""

inp = str(input()).split()
size = int(inp[0])
r = int(inp[1])

pos = []
neg = []
for i in range(size):
    inp = str(input()).split()
    a = int(inp[0])
    b = int(inp[1])
    if b >= 0: pos.append((a, b))
    else: neg.append((a,b))
pos = sorted(pos)
projects = 0
for ab in pos:
    a, b = ab
    if r >= a:
        r += b
        projects += 1
    else: break

neg = sorted(neg, key = lambda ab: ab[0] + ab[1], reverse = True)
n = len(neg)
dp = [[0]*(r + 1) for _ in range(n + 1)]
dp[0][r] = projects
for i in range(0, n):
    for j in range(0, r + 1):
        if j >= neg[i][0] and j + neg[i][1] >= 0:
            dp[i + 1][j + neg[i][1]] = max(dp[i + 1][j + neg[i][1]], dp[i][j] + 1)
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

print(max(dp[n]))
