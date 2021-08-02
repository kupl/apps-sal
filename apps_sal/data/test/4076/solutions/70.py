import math
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = 60 * c + d
f = abs(0.5 * e - 6 * e)
f = f % 360
if f > 180:
    f = 360 - f
print(math.sqrt(a * a + b * b - 2 * a * b * (math.cos(math.radians(f)))))
