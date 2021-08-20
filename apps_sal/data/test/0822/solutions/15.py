(n, m, z) = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def nok(a, b):
    return a // gcd(a, b) * b


print(z // nok(n, m))
