mod = 998244353
fact = [1]
for i in range(1, 2 * 10**5 + 1):
    fact.append((fact[-1] * i) % mod)
revfact = [1]
for i in range(1, 2 * 10**5 + 1):
    revfact.append(pow(fact[i], mod - 2, mod))
n, m, k = map(int, input().split())
ans = 0
for i in range(k, -1, -1):
    group = n - i
    tmp = fact[n - 1] * revfact[group - 1] * revfact[n - 1 - (group - 1)]
    tmp %= mod
    tmp *= m
    tmp %= mod
    tmp *= pow(m - 1, group - 1, mod)
    ans += tmp
    ans %= mod
print(ans)
