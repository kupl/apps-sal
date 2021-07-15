import os

N = int(3e5 + 233)
MOD = 998244353
ans = []
for i in range(N):
    ans.append(0)

def fp(x, y):
    res = 1
    while y:
        if y&1:
            res = res * x
            res %= MOD
        x *= x
        x %= MOD
        y >>= 1
    return res

inv = fp(100, MOD-2)
n = int(input())
dig = list(map(int, input().split()))
for i in range(1, n+1):
    x = dig[i-1]
    x *= inv
    x %= MOD
    ans[i] = (((1 + ans[i-1]) % MOD) * fp(x, MOD-2)) % MOD
print(ans[n])
