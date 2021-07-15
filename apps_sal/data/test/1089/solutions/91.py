H, W, K = list(map(int, input().split()))
MOD = 10 ** 9 + 7

factorial = [1, 1]  # 元テーブル
inverse = [1, 1]  # 逆元テーブル
inverse_from = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, H * W + 1):
    factorial.append((factorial[-1] * i) % MOD)
    inverse_from.append((-inverse_from[MOD % i] * (MOD // i)) % MOD)
    inverse.append((inverse[-1] * inverse_from[-1]) % MOD)


def nCr(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD


ans = 0
# Hについて
for d in range(1, H):
    ans += d * (H - d) * pow(W, 2, MOD) * nCr(H * W - 2, K - 2) % MOD
    ans %= MOD
# Wについて
for d in range(1, W):
    ans += d * (W - d) * pow(H, 2, MOD) * nCr(H * W - 2, K - 2) % MOD
    ans %= MOD

print((ans % MOD))

