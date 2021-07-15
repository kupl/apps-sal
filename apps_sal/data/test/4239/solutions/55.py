#coding: utf-8

N = int(input())

dp = [i for i in range(N+1)]

dp[0] = 0

for i in range(N+1):
    for amount in (6, 9):
        a = amount 
        while i + a < len(dp):
            dp[i + a] = min(dp[i + a], dp[i] + 1)
            a *= amount

print((dp[N]))


