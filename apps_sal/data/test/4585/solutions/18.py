ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

x = ni()
tmp = 0
for i in range(1,10**9):
    tmp+=i
    if tmp>=x:
        break
print(i)

