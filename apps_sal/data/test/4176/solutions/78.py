a, b = [int(x) for x in input().split()]


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


print(a * b // gcd(a, b))
