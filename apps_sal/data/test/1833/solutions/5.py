from sys import stdin
import math


def nextDiv(a):
    ret = []
    i = 1
    while i * i <= a:
        if a % i == 0:
            ret.append(i)
            j = a // i
            if i != j:
                ret.append(j)
        i += 1
    return ret[::-1]


MOD = int(1000000000.0 + 7)


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
