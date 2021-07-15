import sys, math,os
from io import BytesIO, IOBase
#data = BytesIO(os.read(0,os.fstat(0).st_size)).readline
# from bisect import bisect_left as bl, bisect_right as br, insort
# from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
# from decimal import Decimal
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
#sys.setrecursionlimit(100000 + 1)
INF = 10**9
mod = 998244353

step=[(1,0),(-1,0),(0,1),(0,-1)]

n=int(data())
a=mdata()
a1=[]
for i in range(n):
    a1.append((a[i],i))
a1=sorted(a1)
ans=[]
for i in range(n-1,-1,-1):
    k=0
    while a1[k][1]!=i:
        k+=1
    for j in range(k+1,n):
        if a1[k][1]>a1[j][1]:
            a[a1[k][1]],a[a1[j][1]]=a[a1[j][1]],a[a1[k][1]]
            ans.append(str(a1[j][1]+1)+' '+str(a1[k][1]+1))
flag=True
for i in range(n-1):
    if a[i]>a[i+1]:
        flag=False
        break
if flag==True:
    out(len(ans))
    out('\n'.join(ans))
else:
    out(-1)







