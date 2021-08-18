def prepare(n):
    nonlocal MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs


N, M = map(int, input().split())

MOD = 10 ** 9 + 7
modFacts, invs = prepare(max(N, M))

ans = 0
for i in range(N + 1):
    Ti = (modFacts[N] * invs[i] * invs[N - i]) % MOD
    Ti *= (modFacts[M] * invs[M - i]) % MOD
    Ti %= MOD
    Ti *= pow(modFacts[M - i] * invs[(M - i) - (N - i)], 2, MOD)
    Ti %= MOD
    ans += pow(-1, i) * Ti
    ans %= MOD

print(ans)
