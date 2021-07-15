import math
from functools import reduce

def gcd(*numbers):
  return reduce(math.gcd, numbers)

n, x = map(int, input().split())
xx = list(map(int, input().split()))

a = [abs(x - i) for i in xx]

print(gcd(*a))
