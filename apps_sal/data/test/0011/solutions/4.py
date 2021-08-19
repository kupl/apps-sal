def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    (n, a, b, p, q) = list(map(int, input().split()))
    if a == b:
        print(n // a * max(p, q))
    else:
        print(n // a * p + n // b * q - n // lcm(a, b) * min(p, q))


main()
