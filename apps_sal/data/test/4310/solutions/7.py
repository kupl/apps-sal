A=list(map(int,input().split()))
A.sort()
ans=0
for i in range(2):
    ans+=A[i+1]-A[i]
print(ans)
