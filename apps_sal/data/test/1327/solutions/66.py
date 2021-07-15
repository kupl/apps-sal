ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
pm = [-1,1]

n,m = ma()
xyz = []
for i in range(n):
    xyz.append(lma())

def f(p0,p1,p2):
    xyz.sort(key=lambda x:p0*x[0]+p1*x[1]+p2*x[2],reverse=True)
    ret=0
    for i in range(m):
        t=xyz[i]
        ret+=p0*t[0]+p1*t[1]+p2*t[2]
    return ret
tmp=-10**15
for i in range(2**3):
    p=[1,1,1]
    for j in range(3):
        p[j]= pm[(i >> j) &1]
    #print(p)
    #print(f(*p))
    tmp=max(tmp,f(*p))
print(tmp)

