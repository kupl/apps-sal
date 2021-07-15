import math
a,b,c = map(int, input().split())
x = math.gcd(a , b)
if c % x == 0:
  print("YES")
else:
  print("NO")
