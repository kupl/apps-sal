INF=10**20

import sys
import numpy as np

input=sys.stdin.readline

N=int(input())
direction=["U","D","R","L"]
X={moji:[] for moji in direction}
Y={moji:[] for moji in direction}
for i in range(N):
    x,y,d=input().split()
    x=int(x)
    y=int(y)
    X[d].append(x)
    Y[d].append(y)

query=[]
#Xmax
if not X["L"]:
    Lmax=-INF
else:
    Lmax=max(X["L"])
if not X["R"]:
    Rmax=-INF
else:
    Rmax=max(X["R"])
if not X["U"]:
    mobUmax=-INF
else:
    mobUmax=max(X["U"])
if not X["D"]:
    mobDmax=-INF
else:
    mobDmax=max(X["D"])
UDmax=max(mobUmax,mobDmax)

q1=(Lmax-Rmax)/2
q2=Lmax-UDmax
q3=UDmax-Rmax
if q1>q2:
    query.append([q2,"Xmax",0,UDmax])
    query.append([q3,"Xmax",1,Rmax])
else:
    query.append([q1,"Xmax",1,Rmax])

#Xmin
if not X["L"]:
    Lmin=INF
else:
    Lmin=min(X["L"])
if not X["R"]:
    Rmin=INF
else:
    Rmin=min(X["R"])
if not X["U"]:
    mobUmin=INF
else:
    mobUmin=min(X["U"])
if not X["D"]:
    mobDmin=INF
else:
    mobDmin=min(X["D"])
UDmin=min(mobUmin,mobDmin)


q1=(Lmin-Rmin)/2
q2=UDmin-Rmin
q3=Lmin-UDmin
if q1>q2:
    query.append([q2,"Xmin",0,UDmin])
    query.append([q3,"Xmin",-1,Lmin])
else:
    query.append([q1,"Xmin",-1,Lmin])

#Ymax
if not Y["L"]:
    mobLmax=-INF
else:
    mobLmax=max(Y["L"])
if not Y["R"]:
    mobRmax=-INF
else:
    mobRmax=max(Y["R"])
if not Y["U"]:
    Umax=-INF
else:
    Umax=max(Y["U"])
if not Y["D"]:
    Dmax=-INF
else:
    Dmax=max(Y["D"])
LRmax=max(mobLmax,mobRmax)


q1=(Dmax-Umax)/2
q2=Dmax-LRmax
q3=LRmax-Umax
if q1>q2:
    query.append([q2,"Ymax",0,LRmax])
    query.append([q3,"Ymax",1,Umax])
else:
    query.append([q1,"Ymax",1,Umax])

#Ymin
if not Y["L"]:
    mobLmin=INF
else:
    mobLmin=min(Y["L"])
if not Y["R"]:
    mobRmin=INF
else:
    mobRmin=min(Y["R"])
if not Y["U"]:
    Umin=INF
else:
    Umin=min(Y["U"])
if not Y["D"]:
    Dmin=INF
else:
    Dmin=min(Y["D"])
LRmin=min(mobLmin,mobRmin)

q1=(Dmin-Umin)/2
q2=LRmin-Umin
q3=Dmin-LRmin
if q1>q2:
    query.append([q2,"Ymin",0,UDmin])
    query.append([q3,"Ymin",-1,Dmin])
else:
    query.append([q1,"Xmax",-1,Dmin])

query.sort()
xmax=np.poly1d([-1,Lmax])
xmin=np.poly1d([1,Rmin])
ymax=np.poly1d([-1,Dmax])
ymin=np.poly1d([1,Umin])

val=[]
for i in range(-1,len(query)-1):
    if i==-1:
        p=(xmax-xmin)*(ymax-ymin)
        coef2d=p.coef[0]
        coef1d=p.coef[1]
        if coef2d>0:
            minval=coef1d/(2*coef2d)
            next=query[i+1][0]
            if minval>=0 and next>minval:
                val.append(minval)
    else:
        t,func,c2d,c1d=query[i]
        if func=="Xmax":
            xmax=np.poly1d([c2d,c1d])
        if func=="Xmin":
            xmin=np.poly1d([c2d,c1d])
        if func=="Ymax":
            ymax=np.poly1d([c2d,c1d])
        if func=="Ymin":
            ymin=np.poly1d([c2d,c1d])
        p=(xmax-xmin)*(ymax-ymin)
        if p.order==2:
            coef2d=p.coef[0]
            coef1d=p.coef[1]
            if coef2d>0:
                minval=coef1d/(2*coef2d)
                next=query[i+1][0]
                if minval>=0 and next>minval:
                    val.append(minval)
def Xmax(t):
    return max(UDmax,Rmax+t,Lmax-t)
def Xmin(t):
    return min(UDmin,Rmin+t,Lmin-t)
def Ymax(t):
    return max(LRmax,Umax+t,Dmax-t)
def Ymin(t):
    return min(LRmin,Umin+t,Dmin-t)

def function(t):
    return (Xmax(t)-Xmin(t))*(Ymax(t)-Ymin(t))

ans=function(0)
ppp=0
for i in range(0,len(val)):
    if 10**8>=val[i]>=0:
        if ans>function(val[i]):
            ans=min(ans,function(val[i]))
            ppp=val[i]

for i in range(0,len(query)):
    if 10**8>=query[i][0]>=0:
        if ans>function(query[i][0]):
            ans=min(ans,function(query[i][0]))
            ppp=query[i][0]

print(ans)
