from math import atan2, degrees
(a, b, x) = list(map(int, input().split()))
if a * a * b / 2 >= x:
    c = 2 * x / a / b
    print(degrees(atan2(b, c)))
else:
    c = 2 * x / a / a - b
    print(degrees(atan2(b - c, a)))
