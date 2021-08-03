import math

a, b, x = map(int, input().split())

if x >= a * a * b / 2:
    tan = ((a * a * b - x) * 2) / a**3
    print(math.degrees(math.atan(tan)))

else:
    tan = 2 * x / (a * b * b)
    print(90 - math.degrees(math.atan(tan)))
