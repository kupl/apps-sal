MOD = 10 ** 9 + 7
N, K = list(map(int, input().split()))
d = [0] * (K + 1)
for i in range(1, K + 1):
    d[i] = pow(K // i, N, MOD)
for i in reversed(list(range(1, K + 1))):
    for j in range(2 * i, K + 1, i):
        d[i] -= d[j]
        d[i] %= MOD
ans = 0
for i in range(1, K + 1):
    ans += d[i] * i
    ans %= MOD
print(ans)

