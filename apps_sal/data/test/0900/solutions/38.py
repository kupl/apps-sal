import math
import heapq
import bisect
MOD = 10 ** 9 + 7
S = input()
ans = [0] * 13
ans[0] = 1
for c in S:
    dp = [0] * 13
    for i in range(13):
        dp[i * 10 % 13] = ans[i] % MOD
    dp += dp
    if c == '?':
        for i in range(13):
            ans[i] = sum(dp[i + 4:i + 14])
    else:
        for i in range(13):
            ans[i] = dp[i + 13 - int(c)]
print(ans[5] % MOD)
