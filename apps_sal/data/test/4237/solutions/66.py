import math
(a, b, c, d) = list(map(int, input().split()))
s1 = b // c - (a - 1) // c
s2 = b // d - (a - 1) // d
s12 = b // (c * d // math.gcd(c, d)) - (a - 1) // (c * d // math.gcd(c, d))
print(b - a + 1 - (s1 + s2 - s12))
