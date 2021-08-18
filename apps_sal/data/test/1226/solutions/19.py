n, a, b = map(int, input().split())
MOD = 10**9 + 7

ans = pow(2, n, MOD) - 1
a, b = min(a, b), max(a, b)

tmp = 1
for i in range(1, a + 1):
    tmp = tmp * (n + 1 - i) * pow(i, -1, MOD)
    tmp %= MOD
ans = (ans - tmp) % MOD
for i in range(a + 1, b + 1):
    tmp = tmp * (n + 1 - i) * pow(i, -1, MOD)
    tmp %= MOD
ans = (ans - tmp) % MOD

print(ans)
