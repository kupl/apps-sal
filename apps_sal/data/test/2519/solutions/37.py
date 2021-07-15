n,k=map(int,input().split())
l=list(map(int,input().split()))

for i in range(n):
  l[i]=(l[i]+1)/2

lis=[0]*(n+1)
for i in range(n):
  lis[i+1]=lis[i]+l[i]
  
ans=0
for i in range(n-k+1):
  num=lis[i+k]-lis[i]
  ans=max(num,ans)
  
print(ans)
