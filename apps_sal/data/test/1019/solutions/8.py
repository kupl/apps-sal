n = int(input())


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    elif a == 0:
        return b
    elif a == 1:
        return 1
    else:
        return gcd(b % a, a)


if n % 2 != 0:
    print(n // 2, n - n // 2)
else:
    c = n // 2
    while gcd(c, n - c) > 1:
        c -= 1
    print(c, n - c)
