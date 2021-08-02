N, K = map(int, input().split())
M = N - K
MOD = 10 ** 9 + 7

f = [1] * (N + 1)
for i in range(1, N + 1):
    f[i] = f[i - 1] * i

for i in range(1, K + 1):
    ans = f[M + 1] // (f[i] * f[M + 1 - i])
    ans %= MOD
    ans *= (f[K - 1] // (f[i - 1] * f[K - i]))
    ans %= MOD
    print(ans)
