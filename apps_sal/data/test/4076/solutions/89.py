import math

a, b, h, m = list(map(int, input().split()))

ang = abs(h * 30 - m * 11/2)
angle = min(ang, 360-ang)

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))

print(c)

