(n, k) = map(int, input().split())


def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    lcm = x * y // gcd(x, y)
    return lcm


print(lcm(n, 10 ** k))
