N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(M)]
c=[[] for i in range(N)]
for a,b in AB:
    c[a-1].append(b-1)
from collections import deque
import sys
sys.setrecursionlimit(10**9)
def f2(q):
    s=set(q)
    for a,b in AB:
        if a in s and b in s:
            i=q.index(b)
            if q[i-1]!=a:
                break
    if a in s and b in s and q[i-1]!=a:
        q2=deque([a,b])
        while q[(i+1)%len(q)]!=a:
            q2.append(q[(i+1)%len(q)])
            i+=1
        f2(q2)
    print(len(q),*q,sep='\n')
    return
v=[0]*N 
w=[0]*N
def f(p,v,q):
    v[p]=1
    w[p]=1
    q.append(p+1)
    for n in c[p]:
        if v[n]:
            f2(q)
        else:
            f(n,v,q)
    q.pop()
    v[p]=0
for p in range(N):
    if w[p]==0:
        f(p,v,deque())
print(-1)

