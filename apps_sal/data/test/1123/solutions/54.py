N, K = list(map(int, input().split()))
d = [0] * (K + 1)
MOD = 10**9 + 7
for i in range(1, K + 1):
    d[i] = pow(K // i, N, MOD)
for i in range(K, 0, -1):
    for j in range(2 * i, K + 1, i):
        d[i] -= d[j]
        d[i] %= MOD
ans = 0
for i in range(1, K + 1):
    ans += d[i] * i
    ans %= MOD
print(ans)
