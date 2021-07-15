import math

a, b, h,m = list(map(int,input().split()))

h_deg = (60 * h + m) * (360 / (60*12))
m_deg = m * (360 / 60)
deg = abs(h_deg-m_deg)
rad = math.radians(deg)

c = a ** 2 + b ** 2 - 2 * a * b  * math.cos(rad)

print((math.sqrt(c)))


