import math
(a, b, h, m) = map(int, input().split())
m_radians = 360 * m / 60
h_radians = 360 * ((h * 5 + 5 * m / 60) / 60)
cos_ab = math.cos(math.radians(h_radians - m_radians))
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * cos_ab)
print(c)
