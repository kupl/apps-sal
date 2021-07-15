ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
mod=10**9+7
L = input()
n = len(L)
dp1 = [0]*n#i桁目までがLより小さい
dp2=[0]*n#i桁目までがLと一致
dp1[0]=1 #00
dp2[0]=2 #01 or 10
for i in range(1,n):
    if L[i]=="1":
        dp1[i] = (2+1)*dp1[i-1]+1*dp2[i-1]
        dp2[i]= 2*dp2[i-1]
    elif L[i]=="0":
        dp1[i]=(2+1)*dp1[i-1]
        dp2[i]=dp2[i-1]
    dp1[i]%=mod
    dp2[i]%=mod
print((dp1[n-1]+dp2[n-1])%mod)

