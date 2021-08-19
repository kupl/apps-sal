(n, a, b) = list(map(int, input().split()))
mod = pow(10, 9) + 7


def comb(N, x):
    numerator = 1
    for i in range(N - x + 1, N + 1):
        numerator = numerator * i % mod
    denominator = 1
    for j in range(1, x + 1):
        denominator = denominator * j % mod
    d = pow(denominator, mod - 2, mod)
    return numerator * d % mod


a = comb(n, a)
b = comb(n, b)
print((pow(2, n, mod) - 1 - a - b) % mod)
