def gcd(a, b):
    while b:
        a %= b
        (a, b) = (b, a)
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    (n, m, z) = list(map(int, input().split()))
    q = lcm(n, m)
    print(z // q)


main()
