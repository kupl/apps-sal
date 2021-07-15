n = int(input())
from fractions import gcd
g = int(input())
for i in range(n-1):
  h = int(input())
  g = g * h // gcd(g,h)
print(g)
