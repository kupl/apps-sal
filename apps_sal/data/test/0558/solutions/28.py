# from math import factorial
n,m,k = map(int, input().split())
if m == 1:
    if k == n-1:
        print(1)
    else:
        print(0)
    return
MOD = 998244353

ans = tmp = (m * (m-1) ** (n-1)) % MOD

for i in range(k):
    tmp *= (n-1-i)
    tmp %= MOD
    tmp *= pow((m-1) * (i+1), -1, MOD)
    ans += tmp
    ans %= MOD

print(ans)
