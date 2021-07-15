#!/bin/python3
import sys
mod = 10 **9 + 7
n = int(input())
s = input()
cnt = list(map(int, input().split()))
dp = [0]
for i in range(0,n):
    dp.append(0)
dp[0] = 1
ans2 = 1
for i in range(1,n + 1):
    o = i -1
    ml = cnt[ord(s[o]) - ord('a')]
    l = 1
    while ml >= l and o >= 0:
        dp[i] += dp[o] 
        dp[i] = dp[i] % mod
        if l > ans2:
            ans2 = l
        l += 1
        o -= 1
        ml = min(ml, cnt[ord(s[o]) - ord('a')])
ans1 = dp[n] % mod
ans3 = 0
ml = n
l = 0
for i in range(n):
    ml = min(ml,cnt[ord(s[i]) - ord('a')])
    l+=1
    if l > ml:
        ans3+=1
        l = 1
        ml = cnt[ord(s[i]) - ord('a')]
ans3 += 1
print(ans1)
print(ans2)
print(ans3)
