M = 0x3b9aca07
rd = lambda: list(map(int, input().split()))
inv = lambda x: (M - M // x) * inv(M % x) % M if x - 1 else 1
n, k = rd()
w = sum(rd()) % M
modinv = [0, 1]
for i in range(2, 200005):
    modinv.append((M - M // i) * modinv[M % i] % M)
f = [1, -1]
fa_inv = [1]
for i in range(1, 200005):
    fa_inv.append(fa_inv[-1] * modinv[i] % M)


def sti(n, m):
    r = 0
    if n >= m:
        for i in range(m + 1):
            r = (r + f[i & 1] * fa_inv[m - i] * fa_inv[i] * pow(m - i, n, M)) % M
    return r


print(w * (sti(n, k) + (n - 1) * sti(n - 1, k)) % M)
