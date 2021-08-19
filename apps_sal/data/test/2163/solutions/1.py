import math


def euclid_algorithm(a, b):
    t1, t2 = abs(a), abs(b)
    # saving equalities:
    #t1 == x1 * a + y1 * b,
    # t2 == x2 * a + y2 * b.
    x1, y1, x2, y2 = int(math.copysign(1, a)), 0, 0, int(math.copysign(1, b))
    if t1 < t2:
        t1, t2 = t2, t1
        x1, y1, x2, y2 = x2, y2, x1, y1

    while t2 > 0:
        k = int(t1 // t2)
        t1, t2 = t2, t1 % t2
        #t1 - k * t2 == (x1 - k * x2) * a + (y1 - k * y2) * b
        x1, y1, x2, y2 = x2, y2, x1 - k * x2, y1 - k * y2

    return t1, x1, y1


def opposite_element(x, p):
    gcd, k, l = euclid_algorithm(x, p)
    if gcd != 1:
        return -1
    return k % p


def solve(n, m, p):
    if (m - 1) % p == 0:
        return (n + 1) * pow(m, n, p) % p
    else:
        S = pow(m, n, p)
        k = opposite_element(m, p)
        l = (2 * m - 1) * k % p
        q = opposite_element(l - 1, p)
        S += pow(m, n, p) * (pow(l, n, p) - 1) * q
        S %= p
        return S


p = 10 ** 9 + 7
n, m = [int(x) for x in input().split()]
print(solve(n, m, p))
