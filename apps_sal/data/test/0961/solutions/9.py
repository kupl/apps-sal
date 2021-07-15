#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n=int(input())
a=input()
b=list(map(int,a.strip().split()))
L={}
R={}
vis={}
dp=[]
for i in range(n):
    if L.get(b[i])==None:
        L[b[i]]=i
    R[b[i]]=i
    dp.append(0)
dp.append(0)
for i in range(n):
    vis.clear()
    if i>0:
        dp[i]=dp[i-1]
    ans=0
    Min=i
    j=i
    while j>=0:
        t=b[j]
        if vis.get(t)==None:
            if R[t]>i:
                break
            Min=min(Min,L[t])
            ans^=t
            vis[t]=1
        if j<=Min:
            dp[i]=max(dp[i],dp[j-1]+ans)
        j-=1
print(dp[n-1])



