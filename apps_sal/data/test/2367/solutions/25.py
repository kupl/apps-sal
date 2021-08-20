(h, w, a, b) = map(int, input().split())
inv = [0] * (2 * max(h, w) + 1)
fact = [0] * (2 * max(h, w) + 1)
inv[0] = 1
fact[0] = 1
mod = 10 ** 9 + 7
for i in range(1, 2 * max(h, w) + 1):
    fact[i] = fact[i - 1] * i % mod
inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(2 * max(h, w), 0, -1):
    inv[i - 1] = inv[i] * i % mod
ans = 0
for yoko in range(b + 1, w + 1):
    re = fact[yoko - 1 + h - 1 - a] * inv[h - 1 - a] * inv[yoko - 1] % mod
    rr = fact[w - yoko + a - 1] * inv[w - yoko] * inv[a - 1] % mod
    ans = (ans + re * rr % mod) % mod
print(ans)
