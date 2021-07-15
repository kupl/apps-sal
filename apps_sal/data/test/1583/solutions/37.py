import math
a,b,x=map(int,input().split())
s=a*a*b
if x>=s/2:
  tmp=(s-x)/a/a*2
  print(math.degrees(math.atan(tmp/a)))
else:
  tmp=x/a/b*2
  print(90.0-math.degrees(math.atan(tmp/b)))
