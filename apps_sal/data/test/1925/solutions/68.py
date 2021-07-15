import math
import decimal

a,b,n=map(int,input().split())

if b<=n:
  x=decimal.Decimal(a*(b-1)/b)
  c=math.floor(x)
  print(c)

else:
  x=decimal.Decimal(a*n/b)
  c=math.floor(x)
  print(c)
