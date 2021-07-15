ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

s = input()
idxs = [[] for i in range(26)]
def wid(w):
    return ord(w)-ord("a")
for i in range(len(s)):
    w = s[i]
    idxs[wid(w)].append(i)
a=-1
b=-1
for i in range(26):
    if len(idxs[i])>=2:
        prev = idxs[i][0]
        for nex in idxs[i]:
            d = nex-prev
            if 1<=d<=2:
                a=prev+1
                b=nex+1
                break
            prev=nex
print(a,b)

