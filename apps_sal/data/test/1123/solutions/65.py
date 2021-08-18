N, K = map(int, input().split())
MOD = 10**9 + 7
ls = [0] * (K + 1)
for i in range(1, K + 1)[::-1]:
    ls[i] = pow(K // i, N, MOD)
    if K // i != 1:
        a = K // i
        for j in range(2, a + 1):
            ls[i] -= ls[i * j]

ans = 0
for i in range(1, K + 1):
    ans += i * ls[i]
    ans %= MOD
print(ans)
