import numpy as np
import sys


def input():
    return sys.stdin.readline()[:-1]


MOD = 1000000007
S = [int(x) if x != '?' else -1 for x in input()]
n = len(S)
r = [0] * 13
s = S[0]
if s != -1:
    r[s] = 1
else:
    for i in range(10):
        r[i] = 1
for i in range(1, n):
    dp = [0] * 26
    for j in range(13):
        dp[j * 10 % 13] += r[j] % MOD
    dp[13:26] = dp[0:13]
    r = [0] * 13
    s = S[i]
    if s == -1:
        w = sum(dp[4:14])
        for j in range(13):
            r[j] += w
            w += dp[j + 1] - dp[j + 4]
    else:
        for j in range(13):
            r[j] += dp[13 - s + j]
print(r[5] % MOD)
