import math
(n, R) = [int(x) for x in input().split()]
phi = math.pi / (2 * n)
A = math.sin(2 * phi) * (math.cos(2 * phi) - math.sin(2 * phi) * math.tan(math.pi / 2 - 3 * phi))
print(n * R * R * A)
