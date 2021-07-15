N=int(input())
P=list(map(int,input().split()))
m=N
ans=0
for i in range(N):
    if m>=P[i]:
        ans+=1
    m=min(m,P[i])
print(ans)

