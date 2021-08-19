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


def solve(n, k):
    if n < 70 and k > (1 << n):
        return (1, 1)
    s, l = 0, k - 1
    while l > 0:
        l >>= 1
        s += l

    p = 10 ** 6 + 3
    x = pow(2, n, p)
    t = pow(opposite_element(2, p), s, p)
    q = (pow(2, n * (k - 1), p) * t) % p
    r = 1
    if k > p:
        r = 0
    else:
        for i in range(1, k):
            r *= (x - i)
            r %= p

    return ((q - r * t) % p, q)


n, k = list(map(int, input().split()))
x, y = solve(n, k)
print(x, y)
