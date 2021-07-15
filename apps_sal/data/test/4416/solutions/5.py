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

n,k=mdata()
a,b,c,d=[],[],[],[]
for i in range(n):
    t1,a1,b1=mdata()
    if a1==1 and b1==1:
        c.append(t1)
    elif a1==1:
        a.append(t1)
    elif b1==1:
        b.append(t1)
    else:
        d.append(t1)
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
d.sort(reverse=True)
ans=0
while k:
    if len(a)!=0 and len(b)!=0:
        if len(c)!=0:
            if c[-1]<a[-1]+b[-1]:
                ans+=c.pop()
            else:
                ans+=a.pop()+b.pop()
        else:
            ans += a.pop() + b.pop()
    elif len(c)!=0:
        ans += c.pop()
    else:
        break
    k-=1
if k!=0:
    out(-1)
else:
    out(ans)


