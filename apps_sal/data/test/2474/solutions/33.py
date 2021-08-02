N, *C = map(int, open(0).read().split())
MOD = 10**9 + 7
p2 = [1] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    p2[i] = p2[i - 1] * 2 % MOD
C.sort()
ans = 0
for i, c in enumerate(C):
    n = N - 1 - i
    ans += c * (n * p2[n - 1] + p2[n]) * p2[N + i] % MOD
print(ans % MOD)
