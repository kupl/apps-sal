(a, b, c, d) = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


e = c * d // gcd(c, d)
print(b - a - b // c + (a + c - 1) // c - b // d + (a + d - 1) // d + b // e - (a + e - 1) // e)
