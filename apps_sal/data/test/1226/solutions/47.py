def combination(n, r, mod=10**9 + 7):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


mod = 10**9 + 7
N, A, B = list(map(int, input().split()))
ans = pow(2, N, mod) - 1 - combination(N, A) - combination(N, B)
ans %= mod
print(ans)
