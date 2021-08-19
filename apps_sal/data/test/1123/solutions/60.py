MOD = 10 ** 9 + 7
(n, k) = map(int, input().split())
d = [0] + [pow(k // i, n, MOD) for i in range(1, k + 1)]
for i in range(k, 0, -1):
    for j in range(2 * i, k + 1, i):
        d[i] -= d[j]
        d[i] %= MOD
print(sum((i * d[i] % MOD for i in range(1, k + 1))) % MOD)
