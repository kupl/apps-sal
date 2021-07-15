n, m = [int(x) for x in input().split(" ")]
MOD = int(1e9 + 7)


fact = [0 for _ in range(m + 1)]
fact[0] = 1
for i in range(1, m + 1):
    fact[i] = fact[i-1] * i % MOD

finv = [0 for _ in range(m + 1)]
finv[m] = pow(fact[m], MOD-2, MOD)
for i in range(m-1, -1, -1):
    finv[i] = finv[i+1] * (i + 1) % MOD

def nCk(n, k):
    return fact[n] * finv[k] * finv[n-k] % MOD

def nPk(n, k):
    return fact[n] * finv[n-k] % MOD

ans = 0
for k in range(0, n + 1):
    tmp = nCk(n, k) * nPk(m, k) * (nPk(m-k, n-k) ** 2)
    if k % 2 == 0:
        ans += tmp
    else:
        ans -= tmp
    ans = ans % MOD

print(ans)


