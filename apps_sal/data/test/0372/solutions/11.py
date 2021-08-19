import decimal
from decimal import Decimal
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
decimal.getcontext().prec = 40


def cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.87758256189
    >>> print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    decimal.getcontext().prec += 2
    (i, lasts, s, fact, num, sign) = (0, 0, 1, 1, 1, 1)
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s


def sin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)

    """
    decimal.getcontext().prec += 2
    (i, lasts, s, fact, num, sign) = (1, 0, x, 1, x, 1)
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s


def acos(x):

    def f(xx):
        return cos(xx) - x
    a = 0
    b = pi
    xx = (a + b) / 2
    fxx = f(xx)
    while abs(fxx) > Decimal('0.0000000000000000000001'):
        if fxx > 0:
            a = xx
        else:
            b = xx
        xx = (a + b) / 2
        fxx = f(xx)
    return xx


def part(ra, rb, d2):
    d = Decimal(d2).sqrt()
    x = (ra ** 2 - rb ** 2 + d2) / (2 * d)
    a = Decimal(acos(x / ra))
    b = Decimal(acos((d - x) / rb))
    part_a = ra ** 2 * a - ra * ra * sin(a) * cos(a)
    part_b = rb ** 2 * b - rb * rb * sin(b) * cos(b)
    return part_a + part_b


(x1, y1, r1) = list(map(int, input().split()))
(x2, y2, r2) = list(map(int, input().split()))
dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
if dist2 > (r1 + r2) ** 2:
    print(0)
elif dist2 <= (r1 - r2) ** 2:
    print(pi * min(r1, r2) ** 2)
else:
    print(part(r1, r2, dist2))
