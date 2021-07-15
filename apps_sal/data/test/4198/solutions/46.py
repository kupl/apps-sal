a,b,x = map(int, input().split())
l,r = 0, 10**9+1
while r-l > 1:
  m = (l+r)//2
  if a*m + b*len(str(m)) <= x:
    l = m
  else:
    r = m
print(l)
