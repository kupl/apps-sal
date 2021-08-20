from fractions import Fraction
T = int(input())


def TMP(h, c, nbH):
    return c + Fraction(nbH, 2 * nbH - 1) * (h - c)


for _ in range(T):
    (h, c, t) = [int(_) for _ in input().split()]
    if t <= (h + c) // 2:
        print(2)
        continue
    (L, R) = (1, 10 ** 9)
    a = 0
    while L <= R:
        m = (L + R) // 2
        tmp = TMP(h, c, m)
        if tmp >= t:
            L = m + 1
            a = m
        else:
            R = m - 1
    b = a + 1
    if abs(TMP(h, c, a) - t) <= abs(TMP(h, c, b) - t):
        print(a * 2 - 1)
    else:
        print(b * 2 - 1)
