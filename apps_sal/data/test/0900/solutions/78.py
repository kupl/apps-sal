#coding: utf-8
import math
import heapq
import bisect

MOD = 10**9+7

S = input()
ans = [1]+[0]*12
 
for c in S:
    dp=[0]*13
    for i in range(13):
        #dpはansを一桁ずらしたもの
        dp[(i*10)%13]=ans[i]%MOD
    #0~12と13~25と同じものを増設
    dp+=dp
 
    if c=='?':
        for i in range(13):
            #添字を13から26まで増やしたから、ここでこう楽な計算ができる。
            ans[i]=sum(dp[i+4:i+14])
    else:
        for i in range(13):
            ans[i]=dp[i+13-int(c)]

print(ans[5]%MOD)
