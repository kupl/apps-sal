n, m, L, R = map(int, input().split())
mod = 998244353
if n * m % 2:
    print(pow(R - L + 1, n * m, mod))
else:
    print((pow(R - L + 1, n * m, mod) + 1 - (R - L) % 2) * pow(2, mod - 2, mod) % mod)
