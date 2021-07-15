n,m=list(map(int,input().split()))
ans=0
for i in range(1,int(m**0.5)+1):
  if m%i>0:continue
  a=i
  b=m//i
  if a*n<=m:ans=max(ans,a)
  if b*n<=m:ans=max(ans,b)
print(ans)

