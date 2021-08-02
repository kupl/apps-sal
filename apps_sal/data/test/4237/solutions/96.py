def gcd(a, b):
    while b: a, b = b, a % b
    return a


def lcm(c, d): return c * d // gcd(c, d)


def div(x):
    num = x
    num -= x // C
    num -= x // D
    num += x // lcm(C, D)
    return num


A, B, C, D = map(int, input().split())
print(div(B) - div(A - 1))
