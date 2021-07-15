from math import *
a,b,x=map(int,input().split())
x=x/a
if x<=a*b/2:
  t=2*x/b
  c=sqrt(b**2+t**2)
  ans=90-degrees(asin(t/c))
else:
  t=2*(a*b-x)/a
  c=sqrt(a**2+t**2)
  ans=90-degrees(asin(a/c))
print(ans)
