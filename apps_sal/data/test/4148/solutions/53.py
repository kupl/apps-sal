ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

n = ni()
s = input()
def wid(w):
    return ord(w)-ord("A")
def ws(wid):
    return chr(wid+ord("A"))
ans = ""
for i in range(len(s)):
    id = (wid(s[i])+n)%26
    ans+=ws(id)
print(ans)

