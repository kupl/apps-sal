import math
a, b, x = map(int, input().split())

x /= a


if x / a / b > 1 / 2:
    tan_th = (a * b - x) * 2 / a**2
else:
    tan_th = (b**2 / 2 / x)
print(math.degrees(math.atan(tan_th)))
