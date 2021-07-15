l,r=list(map(int,input().split()))
m=2019
if l//m<r//m:
  print((0))
else:
  ans=m
  for i in range(l%m, r%m+1):
    for j in range(i+1,r%m+1):
      ans=min(ans,i%m*j%m)
  print(ans)

