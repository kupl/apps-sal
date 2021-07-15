n=int(input())
a=sorted(list(map(int,input().split())))
dp=[0]*(m:=a[-1]+1)
for i in a:
  dp[i]+=1
for i in a:
  for j in range(i*2,m,i):
    dp[j]+=1
ans=0
for i in a:
  if dp[i]==1:
    ans+=1
print(ans)
