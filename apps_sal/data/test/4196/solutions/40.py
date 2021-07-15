import math
from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

fromright = list(accumulate(a, math.gcd))
a.reverse()
fromleft = list(accumulate(a, math.gcd))
fromleft.reverse()

gcd = []

gcd.append(fromleft[1])

for i in range(1, n-1):
  gcd.append(math.gcd(fromright[i-1], fromleft[i+1]))

gcd.append(fromright[n-2])

if n == 2:
  print(max(a))
else:
  print(max(gcd))
