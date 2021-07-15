from math import atan, degrees
a, b, x = list(map(int, input().split()))
if x == a * b * b:
    print((0))
else:
    x = x / a ** 2
    if x >= b / 2:
        print((90-degrees(atan(a / (2 * b - 2 * x)))))
    else:
        print((90-degrees(atan(2 * a * x / b ** 2))))

