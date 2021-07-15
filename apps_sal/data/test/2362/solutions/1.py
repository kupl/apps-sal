from sys import stdin, stdout
from math import *
from heapq import *
from collections import *

dv=list(range(200002))
for i in range(2,200002):
    if ((i*i)>=200002): 
        break
    if (dv[i]==i):
        j=i
        while ((i*j)<200002):
            dv[i*j]=i
            j=j+1
def loPr(x):
    nonlocal dv
    if (x<=1):
        return []
    ret=[]
    while(x>1):
        d=dv[x]
        ret.append(d)
        while(x%d==0):
            x=trunc(x/d)
    return ret
def main():
    nonlocal dv
    n=int(stdin.readline())
    a=[0]+[int(x) for x in stdin.readline().split()]
    e=[]
    for _ in range(n+2):
        e.append([])
    for _ in range(n-1):
        u,v=[int(x) for x in stdin.readline().split()]
        e[u].append(v)
        e[v].append(u)
    
    pre=[0]*(n+2)
    q=[1]
    d=[False]*(n+2)
    d[1]=True
    pre[1]=1
    i=0
    while(i<len(q)):
        u=q[i]
        for v in e[u]:
            if (d[v]==False):
                d[v]=True
                pre[v]=u
                q.append(v)
        i=i+1
    
    f=[dict()]
    for _ in range(n+2):
        f.append(dict())
    b=[[]]
    for i in range(1,n+1):
        b.append(loPr(a[i]))
        for p in b[i]:
            f[i][p]=[1]
    q.reverse()
    res=0
    for u in q:
        nxt=pre[u]
        #print (str(u)+": f=" +str(f[u])+ "  b=" +str(b[u]))
        for p in b[u]:
            fp=f[u].get(p,[1])
            fp.sort()
            res=max(res,fp[-1])
            if (len(fp)>=2):
                res=max(res,fp[-1]+fp[-2]-1)
            fnxt=f[nxt].get(p,None)
            if (fnxt!=None):
                fnxt.append(max(1,fp[-1])+1)
    stdout.write(str(res))
    return 0

def __starting_point():
    main()
__starting_point()
