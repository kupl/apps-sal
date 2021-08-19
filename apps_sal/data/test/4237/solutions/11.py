import math
(a, b, c, d) = map(int, input().split())
lcm = c * d // math.gcd(c, d)
ans = b - a - (b // c - (a - 1) // c + (b // d - (a - 1) // d) - (b // lcm - (a - 1) // lcm)) + 1
print(ans)
