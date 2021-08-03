import math
a, b = map(int, input().split())
lcm = a // math.gcd(a, b) * b
print(lcm)
