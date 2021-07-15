a, b, x, y = list(map(int, input().split()))

from fractions import gcd

x, y = x // gcd(x, y), y // gcd(x, y)

print(min(a // x, b // y))

