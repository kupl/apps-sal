from sys import stdin
import math


def nextDiv(a):
    tmp = set()
    sq = int(math.sqrt(a))
    for i in range(1, sq + 1):
        if (a % i == 0):
            tmp.add(i)
            tmp.add(a // i)

    return reversed(sorted(tmp))


MOD = int(1e9 + 7)


def solve(n, lis):
    dp = [0] * (max(lis) + 1)
    dp[0] = 1

    for i in lis:
        for j in nextDiv(i):
            dp[j] += dp[j - 1]
            dp[j] %= MOD

    return (sum(dp) - 1) % MOD


def intRead():
    while True:
        ln = stdin.readline().strip()
        if not ln:
            return
        for i in map(int, ln.split()):
            yield i


def __starting_point():
    ipt = intRead()
    n = next(ipt)
    lis = [next(ipt) for _ in range(n)]
    print(solve(n, lis))


__starting_point()
