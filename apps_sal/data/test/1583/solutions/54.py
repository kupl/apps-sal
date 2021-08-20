from math import atan2, degrees
(a, b, x) = map(int, input().split())
s = x / a
if x >= a ** 2 * b / 2:
    print(degrees(atan2(2 * (a * b - s) / a, a)))
else:
    print(degrees(atan2(b, 2 * s / b)))
