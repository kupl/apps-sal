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

n = ni()
cnts = []
for i in range(n):
    cnts.append(collections.Counter(list(input())))
ans=""
alp = list("abcdefghijklmnopqrstuvwxyz")
for w in alp:
    tmp=10**10
    for i in range(n):
        tmp = min(tmp,cnts[i][w])
    ans+= w*tmp
print(ans)

