import math
from functools import reduce
a, b = map(int, input().split())
c = list(map(int, input().split()))
d = c[0]
for j in range(a):
    d = math.gcd(d, c[j])
    if d == 1:
        break
e = math.gcd(d, b)
print(b // e)
print(" ".join(str(k) for k in range(b) if k % e == 0))
