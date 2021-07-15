a,b,c,x,y = map(int,input().split())
ans = 0
if a >= c*2:
  y -= x
  ans += c*2*x
  x = 0
if b >= c*2 and y > 0:
  ans += c*2*y
  x -= y
  y = 0
elif a+b >= c*2:
  t = min(max(x,0),max(y,0))
  x -= t
  y -= t
  ans += t*2*c
if y > 0:
  ans += b * y
if x > 0:
  ans += a*x
print(ans)
