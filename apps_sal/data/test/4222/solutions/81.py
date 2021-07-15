#ABC166
n,k=map(int,input().split())
cnt=[0]*(n+1)
for j in range(k):
  tmp = int(input())
  arr=list(map(int,input().split()))
  for val in arr:
    cnt[val]+=1
ans=0
for i in range(1,n+1):
  if cnt[i]==0:
    ans+=1
print(ans)
