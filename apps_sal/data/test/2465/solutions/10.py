import math


for i in range(int(input())):
    angle = int(input()) * 2
    x = math.gcd(angle, 360)
    a, b = angle // x, 360 // x
    while b - a < 2:
        a, b = a * 2, b * 2
    print(b)
