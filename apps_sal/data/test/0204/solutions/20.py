from math import gcd
a, b, x, y = map(int, input().split())
r = gcd(x, y)
x //= r
y //= r
print(min(a // x, b // y))
