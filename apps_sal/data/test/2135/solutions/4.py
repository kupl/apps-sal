__author__ = 'Utena'
h,w=map(int,input().split())
q=[[0]*w for i in range(h)]
for i1 in range(h):
    n0=input()
    for i in range(w):
        if n0[i]=='#':
            q[i1][i]=1
a=[[0]*w for i2 in range(h+1)]
b=[[0]*(w+1) for i3 in range(h)]
for i in range(h):
    for j in range(w-1):
        if q[i][j]==q[i][j+1]==0:
            a[i+1][j+1]=a[i+1][j]+1
        else:
            a[i+1][j+1]=a[i+1][j]
for i in range(1,h+1):
    for j in range(w):
        a[i][j]+=a[i-1][j]
for i in range(h-1):
    for j in range(w):
        if q[i][j]==q[i+1][j]==0:
            b[i+1][j+1]=b[i][j+1]+1
        else:
            b[i+1][j+1]=b[i][j+1]
for i in range(h):
    for j in range(1,w+1):
        b[i][j]+=b[i][j-1]
n=int(input())
for k in range(n):
    r1,c1,r2,c2=list(map(int,input().split()))
    t=a[r2][c2-1]-a[r2][c1-1]-a[r1-1][c2-1]+a[r1-1][c1-1]+b[r2-1][c2]-b[r1-1][c2]-b[r2-1][c1-1]+b[r1-1][c1-1]
    print(t)
