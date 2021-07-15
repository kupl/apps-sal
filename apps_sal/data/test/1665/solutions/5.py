import sys
input=sys.stdin.readline
n=int(input())
L=[[]for i in range(n)]
M=dict()
for i in range(n-1):
    a,b=map(int,input().split())
    M[i]=(a,b)
    L[a-1].append(b)
    L[b-1].append(a)
mxnode=-1
mxdeg=0
for j in range(n):
    if len(L[j])>mxdeg:
        mxdeg=len(L[j])
        mxnode=j+1
mxpt=0
normpt=0
mxedge=list(range(mxdeg))
noredg=list(range(mxdeg,n))
for j in range(n-1):
    if mxnode in M[j]:
        print(mxedge[mxpt])
        mxpt+=1
    else:
        print(noredg[normpt])
        normpt+=1
