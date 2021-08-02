def solve(n, ddd):
    s = sum(ddd)
    if s < 2 * (n - 1):
        return 0

    ans = 1
    MOD = 998244353
    for d in ddd:
        ans = ans * d % MOD

    male = n - 1
    female = s - n

    div = 1
    for i in range(n - 2):
        ans = ans * (male - i) * (female - i) % MOD
        div = div * (i + 1) % MOD

    div = div * (n - 1) % MOD
    ans = ans * pow(div, MOD - 2, MOD) % MOD

    return ans


n = int(input())
ddd = list(map(int, input().split()))

print((solve(n, ddd)))
