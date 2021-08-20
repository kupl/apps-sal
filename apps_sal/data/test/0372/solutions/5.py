from math import cos, sin
from decimal import Decimal, getcontext
getcontext().prec = 100


def sind(x):
    res = x
    xpow = x
    fact = 1
    i = 3
    while True:
        xpow *= -x * x
        fact *= i * (i - 1)
        next_ = res + xpow / fact
        if res == next_:
            break
        res = next_
        i += 2
    return res


def cosd(x):
    res = 1
    xpow = 1
    fact = 1
    i = 2
    while True:
        xpow *= -x * x
        fact *= i * (i - 1)
        next_ = res + xpow / fact
        if res == next_:
            break
        res = next_
        i += 2
    return res


def pi():
    (lb, ub) = (Decimal('3.14'), Decimal('3.15'))
    while True:
        mid = (lb + ub) / 2
        if mid in (lb, ub):
            break
        if sind(mid) < 0:
            ub = mid
        else:
            lb = mid
    return lb


PI = pi()


def acosd(x):
    (lb, ub) = (Decimal(0), PI)
    while True:
        mid = (lb + ub) / 2
        if mid in (lb, ub):
            break
        if cosd(mid) < x:
            ub = mid
        else:
            lb = mid
    return lb


def asind(x):
    (lb, ub) = (-PI / 2, PI / 2)
    while True:
        mid = (lb + ub) / 2
        if mid in (lb, ub):
            break
        if sind(mid) < x:
            lb = mid
        else:
            ub = mid
    return lb


def main():
    (x1, y1, R) = list(map(Decimal, input().split()))
    (x2, y2, r) = list(map(Decimal, input().split()))
    if R > r:
        (x1, x2) = (x2, x1)
        (y1, y2) = (y2, y1)
        (R, r) = (r, R)
    d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)).sqrt()
    if R + r <= d:
        print(0)
        return
    if d + R <= r:
        print(PI * R * R)
        return
    res = Decimal(0)
    res += r * r * acosd((d * d + r * r - R * R) / (2 * d * r))
    res += R * R * acosd((d * d + R * R - r * r) / (2 * d * R))
    res -= ((-d + r + R) * (d + r - R) * (d - r + R) * (d + r + R)).sqrt() / 2
    print(res)


def __starting_point():
    main()


__starting_point()
