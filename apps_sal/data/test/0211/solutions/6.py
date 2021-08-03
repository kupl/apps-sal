MOD = 10 ** 9 + 9
dp = {0: 1, 1: 2}


def two_pow(n):
    if n not in dp:
        dp[n] = (two_pow(n // 2) * two_pow(n // 2)
                 * (2 if n % 2 == 1 else 1) % MOD)
    return dp[n]


n, m, k = list(map(int, input().split()))
fit = n - n // k
if m <= fit:
    print(m)
else:
    a = m - fit
    rem = m - k * a
    print(((two_pow(a + 1) - 2) * k + rem) % MOD)
