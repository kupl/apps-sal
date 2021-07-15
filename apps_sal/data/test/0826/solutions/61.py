n=int(input())

def can(x):
  return x*(x+1)//2<=n+1

l=0
r=n+1

while r-l>1:
  m=(l+r)//2
  if can(m):
    l=m
  else:
    r=m
print(n+1-l)
