N,K=list(map(int,input().split()))
A=[list(map(int,input().split())) for _ in range(N)]
A=sorted(A, key=lambda x: x[0])

cnt=0
for i in range(N):
    a,b=A[i]
    A[i][1]+=cnt
    cnt=A[i][1]

for i in range(N):
    a,b=A[i]
    if K<=b:break
print(a)

