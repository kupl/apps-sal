import math


def resolve():
    a, b, x = map(int, input().split())
    met = a ** 2 * b / 2
    if x > met:
        y = 2 * b - 2 * x / a**2
        ans = math.atan2(y, a)
    elif x == met:
        ans = math.pi / 4
    else:
        y = 2 * x / a / b
        ans = math.pi / 2 - math.atan2(y, b)

    print(math.degrees(ans))


resolve()
