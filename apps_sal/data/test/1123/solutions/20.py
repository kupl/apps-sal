n, k = map(int, input().split())
MOD = 10**9 + 7
l = [0] * (k + 1)
for i in range(k, 0, -1):
    l[i] = pow(k // i, n, MOD)
for i in range(k, 0, -1):
    for j in range(k // i, 1, -1):
        l[i] = (l[i] - l[i * j]) % MOD
ans = 0
for i, c in enumerate(l):
    ans += i * c
    ans %= MOD
print(ans)
