MAXN=10**9+10**5
n,m,w=map(int,input().split())
a=[*map(int,input().split())]
def bs(x):
    incre=[0]*n
    inc_curr=0
    moves=0
    for i in range(n):
        inc_curr-=[0,incre[i-w]][i-w>=0]
        if a[i]+inc_curr<x:
            incre[i]=x-(a[i]+inc_curr)
            inc_curr+=incre[i]
            moves+=incre[i]
        if moves>m:
            return False
    return moves<=m
l=1;r=MAXN
x=0
while l<=r:
    mid=(l+r)//2
    if bs(mid):
        x=mid
        l=mid+1
    else:r=mid-1
print(x)
