ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
cnt = [-1,2,5,5,4,5,6,3,7,6]
n,m = ma()
A = lma()
use=[(cnt[a],a) for a in A]
use.sort(key=lambda x:x[1],reverse=True)
INF=10**9
dp = [0]+[-INF]*(n+10)
for i in range(n):
    if dp[i]==-INF:continue
    for c,a in use:
        dp[i+c]=max(dp[i+c],dp[i]+1)
l = dp[n]
ans = ["0"]*l
num = n
for i in range(l):
    for c,a in use:
        if dp[num-c]==dp[num]-1:
            ans[i]=str(a)
            num-=c
            break
print("".join(ans))

