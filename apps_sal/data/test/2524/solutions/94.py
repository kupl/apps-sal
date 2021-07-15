n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7
ans = 0
for i in range(60):
  keta=1<<i
  cnt=0
  for j in a:
    if keta & j:
      cnt+=1
  ans+=((keta%mod)*cnt*(n-cnt))%mod


print((ans%mod))

