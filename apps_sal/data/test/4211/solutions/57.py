n=int(input())
b=list(map(int,input().split()))
ans=0

ans+=b[0]
for i in range(n-2):
  ans+=min(b[i],b[i+1])
ans+=b[n-2]
print(ans)
