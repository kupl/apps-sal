import math
(a, b, c, d) = list(map(int, input().split()))
lcm = c * d // math.gcd(c, d)
a2 = a - (a // c + a // d - a // lcm)
b2 = b - (b // c + b // d - b // lcm)
print(b2 - a2 if a % c == 0 or a % d == 0 else b2 - a2 + 1)
