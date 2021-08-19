import math
(a, b, c, d) = map(int, input().split())
divc = b // c - (a - 1) // c
divd = b // d - (a - 1) // d
cd = b // (c * d // math.gcd(c, d)) - (a - 1) // (c * d // math.gcd(c, d))
print(b - a - divc - divd + cd + 1)
