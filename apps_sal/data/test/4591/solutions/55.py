# C
A,B,C,X,Y = list(map(int,input().split()))
ans = 0
if 2*C >= A + B:
  ans = A*X+B*Y 
else:
  x = min(X,Y)
  ans = min(X,Y)*(2*C)
  if (X-x)*A + (Y-x)*B > (X+Y-2*x)*(2*C):
    ans += (X+Y-2*x)*(2*C)
  else:
    ans += (X-x)*A + (Y-x)*B
print(ans)

