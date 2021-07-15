import math

a, b, h, m = map(int, input().split())
h_rad = (h * 60 + m) * math.pi / 360
m_rad = m * math.pi / 30
cosine = math.cos(abs(h_rad - m_rad))

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * cosine))
