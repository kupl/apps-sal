N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
c=[list(map(int,input().split())) for _ in range(N)]
X=[(q,w,0) for q,w in a]+[(e,r,1) for e,r in c]
X.sort()
ans=0
dp=[0]*(2*N)
for x,y,z in X:
  if z==0:
    dp[y]+=1
  else:
    for v in range(y-1,-1,-1):
      if dp[v]>0:
        ans+=1
        dp[v]-=1
        break
print(ans)
