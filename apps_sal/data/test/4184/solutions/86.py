N=int(input())
W=list(map(int,input().split()))
x=sum(W)
ans=x
y=0
for i in range(N):
    y+=W[i]
    ans=min(ans,abs(x-2*y))
print(ans)

