import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = input()
    n = len(L)

    res = 0
    cnt = 0
    for i in range(n):
        if L[i] == "1":
            rest = n - (i + 1)
            res += pow(2, cnt, mod) * pow(3, rest, mod) % mod
            res %= mod
            cnt += 1

    res += pow(2, cnt, mod)
    print((res % mod))


def resolve2():
    """
    桁DP
    """
    L = input().rstrip()
    n = len(L)

    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        if L[i - 1] == "0":
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = (dp[i - 1][1] * 3) % mod
        else:
            dp[i][0] = (dp[i - 1][0] * 2) % mod
            dp[i][1] = (dp[i - 1][1] * 3 + dp[i - 1][0]) % mod

    print(((dp[n][0] + dp[n][1]) % mod))


def __starting_point():
    resolve2()


__starting_point()
