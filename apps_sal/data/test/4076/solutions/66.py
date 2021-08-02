import math
a, b, h, m = map(int, input().split())
m_rad = m / 60 * 360
h_rad = (h / 12 * 360) + (m / 60 * 360 / 12)
rad = abs(m_rad - h_rad)
ans = (a**2 + b**2) - (2 * a * b * math.cos(math.radians(rad)))
print(math.sqrt(ans))
