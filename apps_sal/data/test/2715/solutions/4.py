ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys

k = ni()
n = 50
p,r = divmod(k,n)
ans = [0]*n
for i in range(n):
    if i<n-r:
        ans[i]=i + p
    else:
        ans[i]=i+1 + p
print(n)
print(*ans)

