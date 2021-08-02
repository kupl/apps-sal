import math

a, b, c, d = map(int, input().split())

m = b // c + (-a // c)
n = b // d + (-a // d)
g = c * d // math.gcd(c, d)
p = b // g + (-a // g)
print(b - a + 1 - (m + 1 + n + 1 - (p + 1)))
