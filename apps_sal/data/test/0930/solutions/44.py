def nCr_frL(n, r, mod):
    ret = [1, n % mod]
    for i in range(2, r + 1):
        inv = pow(i, mod - 2, mod)
        ret.append((ret[-1] * (n - i + 1) * inv) % mod)
    return ret


N, K = list(map(int, input().split()))
MOD = 10**9 + 7
com1 = nCr_frL(N, N, MOD)
com2 = nCr_frL(N - 1, N - 1, MOD)

if K > N - 1:
    K = N - 1
ans = 0
for m in range(K + 1):
    ans += (com1[m] * com2[N - m - 1]) % MOD
print((ans % MOD))
