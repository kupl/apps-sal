from bisect import bisect_right as br
n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):a[i]*=-1
a.sort()
b=[0]
for i in a:b.append(b[-1]+i)
ng=2*10**5+7
ok=-1
while ok+1!=ng:
  mid=(ng+ok)//2
  co=0
  for i in a:co+=br(a,-(mid+i))
  if co<m:ng=mid
  else:ok=mid
ans=0
co=0
for i in a:
  ind=br(a,-(ok+i)-1)
  co+=ind
  ans+=-b[ind]-i*ind
ans+=(m-co)*ok
print(ans)
