n,m=map(int,input().split())
l=0
r=99999999
for i in range(m):
  a,b=map(int,input().split())
  l=max(l,a)
  r=min(r,b)
if r>=l:
  print(r-l+1)
else:
  print(0)
