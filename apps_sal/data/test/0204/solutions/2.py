from math import gcd
(a, b, x, y) = map(int, input().split())
(x, y) = (x // gcd(x, y), y // gcd(x, y))
print(min(a // x, b // y))
