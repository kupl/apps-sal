n,k=map(int,input().split())
ans=0
for b in range(k+1,n+1):
  r=n%b
  q=n//b
  ans+=(b-k)*q+max(r-max(k-1,0),0)
print(ans)
