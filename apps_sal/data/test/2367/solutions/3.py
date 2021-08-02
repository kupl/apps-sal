H, W, A, B = map(int, open(0).read().split())
MOD = 10**9 + 7

factorials = [1] * (H + W + 1)
inv_factorials = [1] * (H + W + 1)

for i in range(H + W):
    factorials[i + 1] = factorials[i] * (i + 1) % MOD

inv_factorials = list(map(lambda n: pow(n, -1, MOD), factorials))


def modcomb(m, n, mod):
    return factorials[m] * inv_factorials[n] % MOD * inv_factorials[m - n] % MOD


total = modcomb(H + W - 2, W - 1, MOD)

for i in range(B):
    total -= modcomb(H - A - 1 + i, i, MOD) * modcomb(A - 1 + W - 1 - i, W - 1 - i, MOD) % MOD
    total %= MOD

print(total)
