fact = [1]
temp = 1
MOD = 10 ** 9 + 7
for i in range(1, 10 ** 5 + 5):
    temp *= i
    temp %= MOD
    fact += [temp]


def bino(a, b):
    up = fact[a]
    down = pow(fact[b] * fact[a - b], MOD - 2, MOD)
    return up * down % MOD


def find(A):
    MOD = 10 ** 9 + 7
    dp = [0] * (10 ** 5 + 2)
    for x in A:
        dp[x] += 1
    for i in range(2, len(dp)):
        for j in range(2, len(dp)):
            if i * j > len(dp) - 1:
                break
            dp[i] += dp[i * j]
    for i in range(2, len(dp)):
        dp[i] = (pow(2, dp[i], MOD) - 1) % MOD
    for i in range(len(dp) - 1, 1, -1):
        for j in range(2, len(dp)):
            if i * j >= len(dp):
                break
            dp[i] -= dp[i * j]
            dp[i] %= MOD
    ans = 0
    for i in range(2, len(dp)):
        ans += dp[i]
        ans %= MOD
    return (pow(2, len(A), MOD) - ans - 1) % MOD


input()
print(find(list(map(int, input().strip().split(' ')))))
