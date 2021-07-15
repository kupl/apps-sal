MOD = 998244353

n, m, k = map(int, input().split())

fact = [0 for _ in range(n)]
invfact = [0 for _ in range(n)]
fact[0] = 1
for i in range(1, n):
    fact[i] = fact[i - 1] * i % MOD

invfact[n - 1] = pow(fact[n - 1], MOD - 2, MOD)

for i in range(n - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD
def nCk(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fact[n] * invfact[k] * invfact[n - k] % MOD
        
ans = 0
for i in range(0, k + 1):
    ans += m * pow(m - 1, n - i - 1, MOD) * nCk(n - 1, i) % MOD
    
print(ans % MOD)
