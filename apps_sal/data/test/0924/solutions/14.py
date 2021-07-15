import math

a1, b1, c1 = list(map(int, input().split(' ')))
a2, b2, c2 = list(map(int, input().split(' ')))

x = math.gcd(c1, c2)

delta1 = (a1 - a2)
delta1 = delta1 % x
if delta1 < 0:
  delta1 += x

delta2 = (a2 - a1)
delta2 = delta2 % x
if delta2 < 0:
  delta2 += x


a1 = b1 - a1 + 1
a2 = b2 - a2 + 1

sol = max(min(a1 - delta2, a2), min(a1, a2 - delta1))

print(max(0, sol))

