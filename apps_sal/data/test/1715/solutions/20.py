ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

mx = 3*10**10
a,b,q = ma()
S = [0 for i in range(a+2)]
T = [0 for i in range(b+2)]
S[0] = -mx;S[a+1] = mx
T[0] = -mx;T[b+1] = mx
for i in range(a):
    S[i+1]=ni()
for i in range(b):
    T[i+1]=ni()

def bs(x,ls):##ls == S or T
    ok =0
    ng = len(ls)-1
    while ng-ok > 1:
        idx = (ok+ng)//2
        if ls[idx] < x:
            ok = idx
        else:
            ng = idx
    return ok  #xよりも左にあるidxを返す
def solve(x):
    ids = bs(x,S)
    s1 = S[ids] #自分より左
    s2 = S[ids+1] #自分と同じか右
    idt = bs(x,T)
    t1 = T[idt]
    t2 = T[idt+1]

    s1t1 = max(x-s1,x-t1)
    s1t2 = 2*min(x-s1,t2-x) + max(x-s1,t2-x)
    s2t1 = 2*min(s2-x,x-t1) + max(s2-x,x-t1)
    s2t2 = max(s2-x,t2-x)
    print(min(s1t1,s1t2,s2t1,s2t2))

for i in range(q):
    x = ni()
    solve(x)

