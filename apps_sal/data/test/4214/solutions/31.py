import math

def perm(s,a,d,j):
    l=len(s)
    if l==0:
        a.append(d.copy())
    else:
        for i in range(0,l):
            d[j]=s[i]
            perm(s[0:i:]+s[i+1::],a,d,j+1)


def per(N,a):
    """1からNまでの順列のリストを，リストaに作る．dには予めsと同じ長さのリストを用意する"""
    s=list(range(1,N+1))
    d=list(range(1,N+1))
    j=0
    perm(s,a,d,j)

N=int(input())
a=[]
per(N,a)
x=[0]*N
y=[0]*N
for i in range(0,N):
    x[i],y[i]=map(int,input().split())
M=len(a)
S=0
for j in range(0,M):
    for i in range(0,N-1):
        S+=math.sqrt((x[a[j][i]-1]-x[a[j][i+1]-1])**2+(y[a[j][i]-1]-y[a[j][i+1]-1])**2)
print(S/M)
