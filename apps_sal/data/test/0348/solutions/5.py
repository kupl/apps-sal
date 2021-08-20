(n, m, L, R) = list(map(int, input().split()))
mod = 998244353
if n * m % 2 == 1:
    print(pow(R - L + 1, n * m, mod))
else:
    val = pow(R - L + 1, n * m, mod)
    if pow(R - L + 1, n * m, 2) == 0:
        print(val * pow(2, mod - 2, mod) % mod)
    else:
        print(((val - 1) * pow(2, mod - 2, mod) + 1) % mod)
