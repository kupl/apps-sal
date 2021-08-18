"""
Created on Sat Dec 23 03:02:56 2017

@author: sherlock
"""

import array


numbers = list(map(int, input().split()))


n = numbers[0]
d = numbers[1]

dp = []

dp.append(0)

for i in range(1, n):
    dp.append(999999)

s = str(input())

for i in range(1, n):
    if(s[i] == '1'):
        for j in range(1, d + 1):
            if(i - j >= 0):
                dp[i] = min(dp[i - j] + 1, dp[i])


if(dp[n - 1] == 999999):
    print("-1")
else:
    print(dp[n - 1])
