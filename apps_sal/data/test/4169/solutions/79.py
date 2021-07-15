import sys
N,M=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]
A=sorted(A,key=lambda x:x[0])
cost=0
num=0
for i in range(N):
    if num+A[i][1]>M:
        print(cost+A[i][0]*(M-num))
        return
    else:
        cost+=A[i][0]*A[i][1]
        num+=A[i][1]
print(cost)
