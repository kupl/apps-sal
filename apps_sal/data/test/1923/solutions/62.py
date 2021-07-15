# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
L=list(map(int,input().split()))
L.sort(reverse=1)
ans=0
for i in range(N):
    ans+=min(L[i*2],L[i*2+1])
print(ans)
