n=int(input())
s=input()
r=n//2
l=-1
while r-l>1:
  mid=(r+l)//2
  d=dict()
  ok=False
  for i in range(n-mid):
    ss=s[i:i+mid+1]
    if ss not in d:
      d[ss]=i
    else:
      if d[ss]+mid<i:
        ok=True
  if ok:
    l=mid
  else:
    r=mid
print(r)
