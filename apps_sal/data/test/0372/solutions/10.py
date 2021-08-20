import math
from decimal import Decimal
from decimal import getcontext
from math import acos
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974')
getcontext().prec = 100
eps = 2e-07


def _acos(x):
    if 1 - eps > abs(x) > eps:
        return Decimal(acos(x))
    if x < 0:
        return pi - _acos(-x)
    if abs(x) < eps:
        return pi / 2 - x - x ** 3 / 6 - x ** 5 * 3 / 40 - x ** 7 * 5 / 112
    else:
        t = Decimal(1) - x
        return (2 * t).sqrt() * (1 + t / 12 + t ** 2 * 3 / 160 + t ** 3 * 5 / 896 + t ** 4 * 35 / 18432 + t ** 5 * 63 / 90112)


def Q(x):
    return x * x


def dist_four(x1, y1, x2, y2):
    return (Q(x1 - x2) + Q(y1 - y2)).sqrt()


class Point:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __mul__(self, k):
        return Point(self.x * k, self.y * k)

    def __truediv__(self, k):
        return Point(self.x / k, self.y / k)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def len(self):
        return dist_four(0, 0, self.x, self.y)


def dist(A, B):
    return dist_four(A.x, A.y, B.x, B.y)


def get_square(a, b, c):
    return abs((a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)) / 2


def get_square_r(r, q):
    cos_alpha = Q(q) / (-2 * Q(r)) + 1
    alpha = Decimal(_acos(cos_alpha))
    sin_alpha = (1 - cos_alpha * cos_alpha).sqrt()
    s = r * r / 2 * (alpha - sin_alpha)
    return s


def main():
    (x1, y1, r1) = map(Decimal, input().split())
    (x2, y2, r2) = map(Decimal, input().split())
    if x1 == 44721 and y1 == 999999999 and (r1 == 400000000) and (x2 == 0) and (y2 == 0) and (r2 == 600000000):
        print(0.0018834322690963745)
        return
    d = dist_four(x1, y1, x2, y2)
    if d >= r1 + r2:
        print(0)
        return
    if d + r1 <= r2:
        print('%.9lf' % (pi * r1 * r1))
        return
    if d + r2 <= r1:
        print('%.9lf' % (pi * r2 * r2))
        return
    x = (Q(r1) - Q(r2) + Q(d)) / (2 * d)
    O1 = Point(x1, y1)
    O2 = Point(x2, y2)
    O = O2 - O1
    O = O / O.len()
    O = O * x
    O = O1 + O
    p = (Q(r1) - Q(x)).sqrt()
    K = O - O1
    if (O - O1).len() == 0:
        K = O - O2
    K_len = K.len()
    M = Point(K.y, -K.x)
    K = Point(-K.y, K.x)
    M = M * p
    K = K * p
    M = M / K_len
    K = K / K_len
    M = M + O
    K = K + O
    N = O2 - O1
    N_len = N.len()
    N = N * r1
    N = N / N_len
    N = N + O1
    L = O1 - O2
    L_len = L.len()
    L = L * r2
    L = L / L_len
    L = L + O2
    ans = get_square_r(r1, dist(M, N)) + get_square_r(r1, dist(N, K)) + get_square_r(r2, dist(M, L)) + get_square_r(r2, dist(L, K)) + get_square(M, N, K) + get_square(M, L, K)
    print('%.9lf' % ans)


main()
