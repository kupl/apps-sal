n=int(input())
ans=int(0)

A=list(map(int,input().split()))

A.sort()
for i in range(n):
    ans+=A[i]

all=int(0)
for i in range(n):
    all+=A[2*i]
print(max([ans,all]))
