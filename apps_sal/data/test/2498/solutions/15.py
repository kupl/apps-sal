import fractions
import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=lcm_list(map(lambda x: x//2, a))
swt=0

for i in range(n):
  if 0==(b//(a[i]//2))%2:
    swt=1
    break

if 0==swt:
  print(math.ceil((m//b)/2))
else:
  print(0)
