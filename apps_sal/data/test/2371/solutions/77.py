n,z,w=map(int,input().split())
a=list(map(int,input().split()))
if n==1:
  ans=abs(a[0]-w)
else:
  ans=max(abs(a[-1]-a[-2]),abs(a[-1]-w))
print(ans)
