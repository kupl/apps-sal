import sys
sys.setrecursionlimit(10**7)


def main1(n):
    mod = 10**9 + 7
    ret = 0
    memo = {}
    memo[n - 1] = n

    def func(i):
        if i in memo:
            return memo[i]
        if i > n - 1:
            return 1
        ret = 0
        ret += func(i + 1)
        for k in range(2, n + 1):
            ret += func(i + k + 1)
            ret += n - 1
            ret %= mod
        memo[i] = ret
        return ret
    ret = func(0)
    for k in memo:
        print((k, memo[k]))
    return ret


def main2(n):
    mod = 10**9 + 7
    dp = [1] * (2 * n)
    dp[n - 1] = n
    dp[n - 2] = n**2
    now = n - 1
    for i in range(n - 3, -1, -1):
        dp[i] = dp[i + 1]
        now -= dp[i + n + 1]
        now += dp[i + 3]
        dp[i] += now
        dp[i] += (n - 1)**2
        dp[i] %= mod
    return dp[0]


def __starting_point():
    n = int(input())
    ret2 = main2(n)
    print(ret2)


__starting_point()
