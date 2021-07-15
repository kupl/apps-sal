import math

x1, y1, x2, y2 = map(int, input().split())

s = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
a = math.atan2(y2-y1, x2-x1)

x3 = x2 - math.sin(a) * s
y3 = y2 + math.cos(a) * s

x4 = x1 - math.sin(a) * s
y4 = y1 + math.cos(a) * s

print(round(x3), round(y3), round(x4), round(y4))
