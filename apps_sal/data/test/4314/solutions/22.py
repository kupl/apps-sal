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
h,w = ma()
t="."*w
ls=[]
for i in range(h):
    s=input()
    if s!=t:
        ls.append(s)

l = len(ls)
t="."*l
ans = [[] for i in range(l)]
for i in range(w):
    f=False
    for j in range(l):
        if ls[j][i]=="#":
            f=True
    if f:
        for j in range(l):
            ans[j].append(ls[j][i])
for a in ans:
    print("".join(a))

