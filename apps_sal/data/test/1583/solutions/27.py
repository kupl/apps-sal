import math
pi = math.pi


def rtod(rad):
    return 180 / pi * rad


a, b, x = list(map(int, input().split()))


if b / 2 < x / a**2:
    ans = 2 * (a**2 * b - x) / a**3
    ans = math.atan(ans)
    print((rtod(ans)))
else:
    ans = b**2 / (2 * x) * a
    ans = math.atan(ans)
    print((rtod(ans)))
