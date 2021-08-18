def _pow(a, d, md):
    res = 1
    a = a % md
    while d > 0:
        if d & 1:
            res = res * a % md
        d >>= 1
        a = a * a % md
    return res


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 1000000007
p = 1
q = 1
dp = [[0 for i in range(n + 1)] for j in range(2)]
base = 1
dp[0][-1] = 1
dp[1][-1] = 0
for i in range(0, n):
    if a[i] == 0 and b[i] != 0:
        dp[0][i] = dp[0][i - 1] % mod
        dp[1][i] = (dp[1][i - 1] * m + dp[0][i - 1] * (m - b[i])) % mod
        base *= m
        base %= mod
    elif a[i] != 0 and b[i] == 0:
        dp[0][i] = dp[0][i - 1] % mod
        dp[1][i] = (dp[1][i - 1] * m + dp[0][i - 1] * (a[i] - 1)) % mod
        base *= m
        base %= mod
    elif a[i] == 0 and b[i] == 0:
        dp[0][i] = dp[0][i - 1] * m % mod
        dp[1][i] = (dp[1][i - 1] * m * m) % mod
        dp[1][i] += (dp[0][i - 1] * (m - 1) * m // 2) % mod
        base *= m * m
        base %= mod
    elif a[i] != 0 and b[i] != 0:
        if a[i] != b[i]:
            dp[0][i] = 0
            dp[1][i] = dp[1][i - 1] % mod
            if a[i] > b[i]:
                dp[1][i] += dp[0][i - 1] % mod
        else:
            dp[0][i] = dp[0][i - 1] % mod
            dp[1][i] = dp[1][i - 1] % mod

p = dp[1][n - 1]
q = base
p %= mod
q %= mod
q = _pow(q, mod - 2, mod)
print(p * q % mod)
