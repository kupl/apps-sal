ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys
n,T = ma()
ans=10**15
for i in range(n):
    c,t=ma()
    if t<=T:
        ans=min(ans,c)
if ans==10**15:
    print("TLE")
else:print(ans)

