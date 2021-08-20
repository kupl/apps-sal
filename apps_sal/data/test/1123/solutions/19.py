MOD = 10 ** 9 + 7
(N, K) = list(map(int, input().split()))
t = {}
ans = 0
for i in range(K, 0, -1):
    n = pow(K // i, N, MOD)
    for j in range(2 * i, K + 1, i):
        n -= t[j]
    t[i] = n
    ans = (ans + i * n) % MOD
print(ans)
