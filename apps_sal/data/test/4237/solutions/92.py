import math
(a, b, c, d) = map(int, input().split())
split_b = b - b // c - b // d + b // (c * d // math.gcd(c, d))
split_a = a - 1 - (a - 1) // c - (a - 1) // d + (a - 1) // (c * d // math.gcd(c, d))
print(split_b - split_a)
