a = [int(c) for c in input().split()]
N=a[0]
M=a[1]
X=a[2]
A = [int(c) for c in input().split()]
A2 = [0]*(N+1)
for i in range(M):
    A2[A[i]] = 1

cnt = X
cost1 = 0
while cnt < N+1:
    cost1+=A2[cnt]
    cnt+=1

cnt = X
cost2 = 0
while cnt > 0:
    cost2+=A2[cnt]
    cnt-=1

if cost1<cost2:
    print(cost1)
else:
    print(cost2)

