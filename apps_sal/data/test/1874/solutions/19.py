import math
3


a, b, c = list(map(int, input().split()))
v1 = (a ** 3) * (2 ** 0.5) / 12
v2 = (b ** 3) * (2 ** 0.5) / 6

phi = 2 * math.pi / 5
L = c / ((2 - 2 * math.cos(phi)) ** 0.5)
v3 = 2.5 * L * L * math.sin(phi) * ((c * c - L * L) ** 0.5) / 3

print(v1 + v2 + v3)
