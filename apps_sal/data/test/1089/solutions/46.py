(H, W, K) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
factorial = [1, 1]
inverse = [1, 1]
invere_base = [0, 1]
for i in range(2, H * W + 2):
    factorial.append(factorial[-1] * i % MOD)
    invere_base.append(-invere_base[MOD % i] * (MOD // i) % MOD)
    inverse.append(inverse[-1] * invere_base[-1] % MOD)


def nCr(n, r):
    if not 0 <= r <= n:
        return 0
    return factorial[n] * inverse[r] * inverse[n - r] % MOD


ans = 0
for dh in range(1, H):
    ans += dh * (H - dh) * pow(W, 2, MOD) * nCr(H * W - 2, K - 2) % MOD
    ans %= MOD
for dw in range(1, W):
    ans += dw * (W - dw) * pow(H, 2, MOD) * nCr(H * W - 2, K - 2) % MOD
    ans %= MOD
print(ans)
