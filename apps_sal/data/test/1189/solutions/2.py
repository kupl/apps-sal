(n, c) = list(map(int, input().split()))
mod = 10 ** 6 + 3
inv = [0, 1]
for i in range(2, max(n, c) + 1):
    inv.append(inv[mod % i] * (mod - mod // i) % mod)
ans = 1
for i in range(1, n + c + 1):
    ans = ans * i % mod
for i in range(1, c + 1):
    ans = ans * inv[i] % mod
for i in range(1, n + 1):
    ans = ans * inv[i] % mod
ans += mod - 1
ans %= mod
print(ans)
