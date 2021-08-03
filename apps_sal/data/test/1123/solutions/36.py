N, K = map(int, input().split())
MOD = 10**9 + 7

B = [0 for i in range(K + 1)]
for i in range(K + 1)[::-1]:
    if i == 0:
        continue
    B[i] = pow((K // i), N, MOD)
    t = i * 2
    while t <= K:
        B[i] -= B[t]
        t += i

ans = 0
for i in range(K + 1):
    ans += i * B[i]
    ans %= MOD
print(ans)
