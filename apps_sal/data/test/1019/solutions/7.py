n = int(input())

from fractions import gcd
for a in reversed(range(1,n//2+1)):
  b = n-a
  if gcd(a,b) == 1:
    print(a,b)
    break
