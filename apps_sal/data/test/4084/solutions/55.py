n,a,b = map(int,input().split())

q = n//(a+b)
r = n%(a+b)

if r < a:
  ans = a*q + r
else:
  ans = a*q + a
  
print(ans)
