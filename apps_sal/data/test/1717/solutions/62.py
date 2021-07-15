n=int(input())
a=1
from math import gcd
for i in range(2,n+1):
  if a%i:
    g=gcd(a,i)
    a=a*i//g
print(a+1)
