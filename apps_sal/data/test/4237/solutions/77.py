a, b, c, d = map(int, input().split())
a -= 1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


aa = b // c - a // c
bb = b // d - a // d
cc = b // lcm(c, d) - a // lcm(c, d)
print(b - a - (aa + bb - cc))
