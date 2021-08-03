MOD = 10**9 + 7
N, K = map(int, input().split())
d = [0]
d += [pow(K // i, N, MOD) for i in range(1, K + 1)]
for i in reversed(range(1, K + 1)):
    j = 2
    while(i * j <= K):
        d[i] = (d[i] - d[i * j] + MOD) % MOD
        j += 1
ans = 0
for i in range(1, K + 1):
    ans = (ans + d[i] * i % MOD) % MOD
print(ans)
