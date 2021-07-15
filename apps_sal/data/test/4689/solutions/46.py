K,N=map(int,input().split())
A=list(map(int,input().split()))
ans=K-(A[-1]-A[0])
for i in range(N-1):
    tmp=A[i+1]-A[i]
    ans=max(ans,tmp)
ans=K-ans
print(ans)
