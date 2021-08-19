(H, W, A, B) = list(map(int, input().split()))
mod = 10 ** 9 + 7
C = [1, 1]
inv = [0, 1]
Cinv = [1, 1]
for i in range(2, H + W + 1):
    C.append(C[-1] * i % mod)
    inv.append(-inv[mod % i] * (mod // i) % mod)
    Cinv.append(Cinv[-1] * inv[-1] % mod)
ans = 0
for i in range(H - A):
    a = C[i + B - 1] * C[H - 1 - i + W - B - 1] % mod
    a = a * Cinv[B - 1] % mod
    a = a * Cinv[i] % mod
    a = a * Cinv[W - B - 1] % mod
    a = a * Cinv[H - i - 1] % mod
    ans += a
    ans %= mod
print(ans)
