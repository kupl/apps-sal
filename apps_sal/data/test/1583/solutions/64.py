from math import atan, degrees
a, b, x = map(int, input().split())

if a * a * b <= 2 * x:
    theta = degrees(atan(2 * b / a - 2 * x / (a * a * a)))
else:
    theta = degrees(atan(a * b * b / (2 * x)))
print(theta)
