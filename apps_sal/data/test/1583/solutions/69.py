import math

a, b, x = list(map(int, input().split()))

s = x / a

if s >= a * b / 2:
    h = (a * b - s) * 2 / a
    rad = math.atan2(h, a)
else:
    w = s * 2 / b
    rad = math.atan2(b, w)

print((rad / (2 * math.pi) * 360))
