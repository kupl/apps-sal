from math import factorial

MOD = 10**9+7
fact = {}

a, b, n = list(map(int, input().split()))
fact[0]=1
for i in range(1, n+1):
    fact[i] = fact[i-1]*i%MOD

ans = 0
for (i, j) in zip(list(range(n+1)), list(range(n, -1, -1))):
    if set(str(a*i + b*j)) <= {f'{a}', f'{b}'}:
        ans+=(fact[n]*pow(fact[n-i]*fact[i]%MOD, MOD-2, MOD) % MOD)
print(ans%MOD)

