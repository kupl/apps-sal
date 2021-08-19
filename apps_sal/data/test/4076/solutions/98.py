import math
(a, b, h, m) = list(map(int, input().split()))
total_minute = 60 * h + m
ax = a * math.cos(math.radians(360 - total_minute / 2 + 90))
ay = a * math.sin(math.radians(360 - total_minute / 2 + 90))
bx = b * math.cos(math.radians(360 - 6 * m + 90))
by = b * math.sin(math.radians(360 - 6 * m + 90))
kyori = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
print(kyori)
