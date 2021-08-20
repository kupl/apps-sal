(N, M, K) = map(int, input().split())
c = [0 for i in range(N * M)]
c[1] = 1
c[0] = 1
mod = 10 ** 9 + 7
for i in range(1, N * M - 1):
    c[i + 1] = (i + 1) * c[i] % mod


def comb(a, b):
    return c[a] * pow(c[b], mod - 2, mod) * pow(c[a - b], mod - 2, mod) % mod


ans = 0
for i in range(N):
    ans += i * (N - i) * pow(M, 2)
    ans %= mod
for i in range(M):
    ans += i * (M - i) * pow(N, 2) % mod
    ans %= mod
ans *= comb(N * M - 2, K - 2)
ans %= mod
print(ans)
