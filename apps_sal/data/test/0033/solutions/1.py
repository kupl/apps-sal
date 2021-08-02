import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)

# ax+by=c


def extgcd(a, b, c):
    if b == 0: return c, 0
    x, y = extgcd(b, a % b, c)
    return y, x - a // b * y


def first_term(a1, b1, a2, b2):
    g = gcd(a1, a2)
    T = lcm(a1, a2)

    # s*a1+t*a2=b2-b1
    if (b2 - b1) % g != 0: return -(10 ** 100)
    x0 = extgcd(a1 // g, a2 // g, (b2 - b1) // g)[0] * a1 + b1 - T * 10 ** 30

    ok = 10 ** 60
    ng = -1

    while ok - ng > 1:
        mid = (ok + ng) // 2
        val = x0 + T * mid
        k = (val - b1) // a1
        l = (val - b2) // a2

        if k >= 0 and l >= 0:
            ok = mid
        else:
            ng = mid

    return x0 + ok * T


def f(a0, T, v):
    ok = 10 ** 36
    ng = -1

    while ok - ng > 1:
        mid = (ok + ng) // 2

        if a0 + T * mid >= v:
            ok = mid
        else:
            ng = mid

    return ok


a1, b1, a2, b2, L, R = list(map(int, input().split()))

T = lcm(a1, a2)
a0 = first_term(a1, b1, a2, b2)

if a0 == -(10 ** 100):
    print(0)
    return

print(f(a0, T, R + 1) - f(a0, T, L))
