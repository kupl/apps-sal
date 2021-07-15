import math
a, b, x = map(int, input().split())

if a*a*b / 2 > x:
    h = x / b * 2 / a
    deg = math.atan(h/b)
    deg = math.degrees(deg)
    deg = 90 - deg
else:
    x = a*a*b - x
    h = x / a * 2 / a
    deg = math.atan(h/a)
    deg = math.degrees(deg)
print(deg)
