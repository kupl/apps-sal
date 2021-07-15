import math

n, r = list(map(float, input().split()))

pi = math.pi

part = pi / n
s = n * r * r * math.sin(2. * part) / 2.
bad = n * (math.sin(part) * r) ** 2 * math.tan(pi / 2. - 1.5 * part)

print(s - bad)

