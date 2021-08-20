MOD = int(1000000000.0 + 7)
fact = [1]
for i in range(1, int(1000000.0) + 1, 1):
    fact.append(fact[i - 1] * i % MOD)
(A, B, N) = list(map(int, input().split()))
ans = 0
for i in range(N + 1):
    f = A * i + B * (N - i)
    ng = False
    while f:
        t = f % 10
        if t != A and t != B:
            ng = True
            break
        f //= 10
    if ng:
        continue
    ans = (ans + fact[N] * pow(fact[i], MOD - 2, MOD) * pow(fact[N - i], MOD - 2, MOD)) % MOD
print(ans)
