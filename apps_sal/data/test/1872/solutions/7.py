from decimal import *
from math import sin, pi, sqrt


def getRadian(x):
    return x * Decimal(pi) / 180


def area(a, b, c):
    p = (a + b + c) / 2
    return Decimal(sqrt(p * (p - a) * (p - b) * (p - c)))


def __starting_point():
    getcontext().prec = 100
    (n, r) = map(Decimal, input().split())
    beta = 90 / n
    beta_radian = getRadian(beta)
    gamma = 180 / n
    gamma_radian = getRadian(gamma)
    S = r * r * Decimal(sin(beta_radian)) * Decimal(sin(gamma_radian)) / Decimal(sin(beta_radian + gamma_radian))
    print(n * S)


__starting_point()
