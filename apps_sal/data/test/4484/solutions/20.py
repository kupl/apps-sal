n,m=list(map(int,input().split()))
if abs(n-m)>1:
  print((0))
  return

sm=1 if n!=m else 2
while n>0:
  sm=(sm*n)%(10**9+7)
  n-=1
while m>0:
  sm=(sm*m)%(10**9+7)
  m-=1
print(sm)

