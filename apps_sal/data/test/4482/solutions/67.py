N=int(input())
A=[int(x) for x in input().split()]
maxA=max(A)
minA=min(A)
ans=10**9
for i in range(minA,maxA+1):
    kouho=0
    for j in range(N):
        kouho+=(i-A[j])**2
    ans=min(ans,kouho)
print(ans)
