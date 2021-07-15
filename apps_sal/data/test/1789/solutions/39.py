a,b,x,y = map(int,input().split())
ans = 0
if a == b:
  ans = x
if a > b:
  ans = min(x+(a-b-1)*y,x*(2*a-2*b-1))
if a < b:
  ans = min(x+y*(b-a),x*(2*b-2*a+1))
print(ans)
