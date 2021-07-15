def rec(i):
    nonlocal a
    return i
import sys
from collections import Counter
sys.setrecursionlimit(10**6)
#n=int(input())
n,m=list(map(int,input().split()))
a=[[] for i in range(100)]
b=[i for i in range(1,101)]
for i in range(m):
    x,y=list(map(int,input().split()))
    z=b.copy()
    for i0 in z:
        if not(((x-1)>=(y-1)*i0)and((x-1)<y*i0)):
            b.remove(i0)

a=set()
for i0 in b:
    a.add((n-1)//i0)
if len(a)==1:
    print(a.pop()+1)
else:
    print(-1)

