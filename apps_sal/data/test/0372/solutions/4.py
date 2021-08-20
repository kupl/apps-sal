import math
import decimal


def dec(n):
    return decimal.Decimal(n)


def acos(x):
    return dec(math.atan2((1 - x ** 2).sqrt(), x))


def x_minus_sin_cos(x):
    if x < 0.01:
        return 2 * x ** 3 / 3 - 2 * x ** 5 / 15 + 4 * x ** 7 / 315
    return x - dec(math.sin(x) * math.cos(x))


(x_1, y_1, r_1) = map(int, input().split())
(x_2, y_2, r_2) = map(int, input().split())
pi = dec(31415926535897932384626433832795) / 10 ** 31
d_square = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
d = dec(d_square).sqrt()
r_min = min(r_1, r_2)
r_max = max(r_1, r_2)
if d + r_min <= r_max:
    print(pi * r_min ** 2)
elif d >= r_1 + r_2:
    print(0)
else:
    cos_1 = (r_1 ** 2 + d_square - r_2 ** 2) / (2 * r_1 * d)
    acos_1 = acos(cos_1)
    s_1 = r_1 ** 2 * x_minus_sin_cos(acos_1)
    cos_2 = (r_2 ** 2 + d_square - r_1 ** 2) / (2 * r_2 * d)
    acos_2 = acos(cos_2)
    s_2 = r_2 ** 2 * x_minus_sin_cos(acos_2)
    print(s_1 + s_2)
