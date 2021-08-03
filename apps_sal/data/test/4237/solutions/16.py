import math

a, b, c, d = list(map(int, input().split()))

gcd = (c * d) // math.gcd(c, d)

r = b // c + b // d - b // gcd
l = (a - 1) // c + (a - 1) // d - (a - 1) // gcd

print(((b - a) - (r - l) + 1))
