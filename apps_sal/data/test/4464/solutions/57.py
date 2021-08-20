(a, b, c) = [int(x) for x in input().split()]


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


if c % gcd(a, b) == 0:
    print('YES')
else:
    print('NO')
