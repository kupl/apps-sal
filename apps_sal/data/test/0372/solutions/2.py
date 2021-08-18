"""
Codeforces Educational Round 
Problem 600 D. Area of Two Circles' Intersection

@author yamaton
@date 2015-11-30
      2015-12-02
"""

import sys
import math
import fractions


def f(x):
    """
    Compute  x - sin(x) cos(x)  without loss of significance
    """
    if abs(x) < 0.01:
        return 2 * x**3 / 3 - 2 * x**5 / 15 + 4 * x**7 / 315
    return x - math.sin(x) * math.cos(x)


def acos_sqrt(x, sgn):
    """
    Compute acos(sqrt(x)) with accuracy even when |x| is close to 1.
    http://www.wolframalpha.com/input/?i=acos%28sqrt%281-y%29%29
    http://www.wolframalpha.com/input/?i=acos%28sqrt%28-1%2By%29%29
    """
    assert isinstance(x, fractions.Fraction)

    y = 1 - x
    if y < 0.01:
        pp('y < 0.01')
        numers = [1, 1, 3, 5, 35]
        denoms = [1, 6, 40, 112, 1152]
        ans = fractions.Fraction('0')
        for i, (n, d) in enumerate(zip(numers, denoms)):
            ans += y**i * n / d
        assert isinstance(y, fractions.Fraction)
        ans *= math.sqrt(y)
        if sgn >= 0:
            return ans
        else:
            return math.pi - ans

    return math.acos(sgn * math.sqrt(x))


def solve(r1, r2, d_squared):
    r1, r2 = min(r1, r2), max(r1, r2)

    d = math.sqrt(d_squared)
    if d >= r1 + r2:
        return 0.0
    if r2 >= d + r1:
        return math.pi * r1 ** 2

    r1f, r2f, dsq = map(fractions.Fraction, [r1, r2, d_squared])
    r1sq, r2sq = map(lambda i: i * i, [r1f, r2f])
    numer1 = r1sq + dsq - r2sq
    cos_theta1_sq = numer1 * numer1 / (4 * r1sq * dsq)
    numer2 = r2sq + dsq - r1sq
    cos_theta2_sq = numer2 * numer2 / (4 * r2sq * dsq)
    theta1 = acos_sqrt(cos_theta1_sq, math.copysign(1, numer1))
    theta2 = acos_sqrt(cos_theta2_sq, math.copysign(1, numer2))
    result = r1 * r1 * f(theta1) + r2 * r2 * f(theta2)

    pp("d = %.16e" % d)
    pp("cos_theta1_sq = %.16e" % cos_theta1_sq)
    pp("theta1 = %.16e" % theta1)
    pp("theta2 = %.16e" % theta2)
    pp("f(theta1) = %.16e" % f(theta1))
    pp("f(theta2) = %.16e" % f(theta2))
    pp("result = %.16e" % result)

    return result


def pp(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    d_squared = (x1 - x2)**2 + (y1 - y2)**2
    result = solve(r1, r2, d_squared)
    print("%.17f" % result)


def __starting_point():
    main()


__starting_point()
