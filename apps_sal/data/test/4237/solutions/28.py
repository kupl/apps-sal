import math
(a, b, c, d) = map(int, input().split())
e = c * d // math.gcd(c, d)
f = b - (b // c + b // d - b // e)
g = a - 1 - ((a - 1) // c + (a - 1) // d - (a - 1) // e)
print(int(f - g))
