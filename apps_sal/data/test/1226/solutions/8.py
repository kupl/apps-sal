n, a, b = map(int, input().split())
mod = pow(10, 9) + 7
total = pow(2, n, mod)
# print(total)


def comb(m, x):
    numerator = 1
    for i in range(m - x + 1, m + 1):
        numerator = numerator * i % mod
    denominator = 1
    for i in range(1, x + 1):
        denominator = denominator * i % mod
    d = pow(denominator, mod - 2, mod)
    return numerator * d


a = comb(n, a)
b = comb(n, b)
print((total - a - b - 1) % mod)
