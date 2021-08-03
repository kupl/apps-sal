import math

a, b, c, d = map(int, input().split())


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


print((b - b // c - b // d + (b // lcm(c, d))) - ((a - 1) - (a - 1) // c - (a - 1) // d + ((a - 1) // lcm(c, d))))
