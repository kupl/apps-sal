N, M, K = map(int, input().split())
mod = 998244353

inv = [0, 1]
for i in range(2, N):
    inv.append((-inv[mod % i] * (mod // i)) % mod)

if N == 1:
    print(M)
    return

m = [1]
s = 1
for _ in range(N - 1):
    s = s * (M - 1) % mod
    m.append(s)

ncombi = [1]
c = 1
for k in range(K):
    c = c * (N - 1 - k) * inv[k + 1]
    c %= mod
    ncombi.append(c)

ans = 0
for k in range(K + 1):
    ans = ans + m[-k - 1] * ncombi[k]
    ans %= mod

ans = ans * M % mod
print(ans)
