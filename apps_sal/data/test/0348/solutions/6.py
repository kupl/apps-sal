MOD = 998244353

n, m, L, R = map(int, input().split())

dx = R - L + 1

if n * m % 2:
    print(pow(dx, n * m, MOD))

else:
    print((pow(dx, n * m, MOD) + dx % 2) * pow(2, MOD - 2, MOD) % MOD)
