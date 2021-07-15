N=int(input())
a=sorted(list(map(int,input().split())))

ans=10**9
for i in range(a[0],a[-1]+1):
  s=0
  for j in range(N):
    x=(a[j]-i)**2
    s+=x
  ans=min(ans,s)

print(ans)

