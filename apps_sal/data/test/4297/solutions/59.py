import math
n = int(input())
gcd = math.gcd(2, n)
lcm = 2 * n // gcd
print(lcm)
