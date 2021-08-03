import math
a, b, x = list(map(int, input().split()))
sq = a * a * b / 2

if sq >= x:
    A1 = 2 * x / (a * b)
    num = math.atan(b / A1)
else:
    B1 = 2 * x / a**2 - b
    num = math.atan((b - B1) / a)

print((math.degrees(num)))
