(n, a, b) = map(int, input().split())
MOD = 10 ** 9 + 7


def nCk(n, k):
    num = 1
    for i in range(n, n - k, -1):
        num *= i
        num %= MOD
    tmp = 1
    for i in range(1, k + 1):
        tmp *= i
        tmp %= MOD
    num *= pow(tmp, MOD - 2, MOD)
    return num


ans = pow(2, n, MOD) - 1
ans -= nCk(n, a)
ans -= nCk(n, b)
print(ans % MOD)
