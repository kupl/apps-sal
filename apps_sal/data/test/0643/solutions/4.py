import sys


def de(x, y):
    if (x % y == 0):
        return x // y
    return x // y + 1


def euc(a, b):
    if (b == 0):
        return 1, 0
    x, y = euc(b, a % b)
    return -y, -x - y * (a // b)


def solve(x, y, p, q):
    if (q == p):
        if (x == y):
            return 0
        return -1
    if (p == 0):
        if (x == 0):
            return 0
        return -1

    a0, b0 = euc(p, q)
    g = a0 * p - q * b0
    c = x * q - p * y
    if (c % g):
        return -1
    a0 = a0 * (c // g)
    b0 = b0 * (c // g)
    t1 = a0 // q

    t = max(de(b0 - a0, q - p), de(-b0, p))
    a = a0 + q * t
    b = b0 + p * t

    return a


t = int(input())
for it in range(t):
    x, y, p, q = list(map(int, input().split()))
    print(solve(x, y, p, q))
