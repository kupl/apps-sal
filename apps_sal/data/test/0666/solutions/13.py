import math


def fc(a, b, c):
    d = b * b - 4 * a * c
    x = (-b + math.sqrt(d)) / (2 * a)
    return int(x)


n = int(input())
x = fc(1, 1, -2 * n)
y = n - (1 + x) * x // 2
if y == 0:
    print(x)
else:
    print(y)
