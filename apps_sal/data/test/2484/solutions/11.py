n=int(input())
a=list(map(int,input().split()))
l=0
r=1
t=a[0]
ans=0
 
while l<n:
  if r==n:
    ans+=r-l
    l+=1
    continue
  if t+a[r]==t^a[r]:
    t+=a[r]
    r+=1
  else:
    ans+=r-l
    t-=a[l]
    l+=1
print(ans)
