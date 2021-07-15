# coding: utf-8
# Your code here!
S=int(input())

dp=[0 if i<3 else 1 for i in range(S+1)]


for i in range(3,S-1):
    for j in range(i+3,S+1):
        dp[j]+=dp[i]
        dp[j]%=(10**9+7)

print(dp[-1])
