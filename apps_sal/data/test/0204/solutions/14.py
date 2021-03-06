from fractions import gcd


def read_numbers():
    return list(map(int, input().split()))


INF = 1 << 64
(a, b, x, y) = read_numbers()
g = gcd(x, y)
(x, y) = (x // g, y // g)
print(min(a // x, b // y))
