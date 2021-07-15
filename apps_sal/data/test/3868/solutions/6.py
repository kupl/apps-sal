from bisect import *
from sys import *
n,m,k=[int(i) for i in input().split()]
pln=[]
if m==0:
    print(-1)
    return
for i in range(m):
    pln.append([int(i) for i in input().split()])
pln.sort()

grp=[[pln[0]]];gt=0;
for i in range(1,m):
    if pln[i][0]!=pln[i-1][0]:
        gt=gt+1
        grp.append([])
    grp[gt].append(pln[i])
xx=[]
for i in range(len(grp)):
    xx.append(grp[i][0][0])
#print('grp',grp)
#print('xx',xx)

from math import inf
pre=[0]*len(xx)
ct=0 
mincost=[inf]*(n+1);sumcost=inf
for i,x in enumerate(grp):
    for di,fi,ti,ci in x:
        if ti==0:
            if mincost[fi]==inf:
                ct+=1
            if sumcost==inf:
                mincost[fi]=min(mincost[fi],ci)
            else:
                sumcost=sumcost-mincost[fi]
                mincost[fi]=min(mincost[fi],ci)
                sumcost=sumcost+mincost[fi]
    if ct==n and sumcost==inf:
        sumcost=sum(mincost[1:])
    pre[i]=sumcost
#print(pre)

sa=[0]*len(xx)
ct=0 
mincost=[inf]*(n+1);sumcost=inf
grp.reverse()
for i,x in enumerate(grp):
    for di,fi,ti,ci in x:
        if fi==0:
            if mincost[ti]==inf:
                ct+=1
            if sumcost==inf:
                mincost[ti]=min(mincost[ti],ci)
            else:
                sumcost=sumcost-mincost[ti]
                mincost[ti]=min(mincost[ti],ci)
                sumcost=sumcost+mincost[ti]
    if ct==n and sumcost==inf:
        sumcost=sum(mincost[1:])
    sa[i]=sumcost
sa.reverse()
#print(sa)

ans=inf
for l,xxi in enumerate(xx):
    r=bisect_right(xx,xxi+k)
    ansl=pre[l]
    ansr= inf if r==len(xx) else sa[r]
    ans=min(ans,ansl+ansr)
print(ans) if ans!=inf else print(-1)
        
            

