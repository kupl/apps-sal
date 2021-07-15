n,m,x=map(int,input().split())
a=list(map(int,input().split()))
c=x
ans=0
ans1=0
while c:
  ans+=c in a
  c-=1
while x<n:
  ans1+=x in a
  x+=1
print(min(ans,ans1))
