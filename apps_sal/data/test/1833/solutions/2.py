from sys import stdin
import math


def nextDiv(a):
    tmp = []
    sq = int(math.sqrt(a))
    for i in range(1, sq + 1):
        if (a % i == 0):
            j = a // i
            yield j
            if (i != j):
                tmp.append(i)

    while tmp:
        yield tmp.pop()


MOD = int(1e9 + 7)


def solve(n, lis):
    dp = [0] * (max(lis) + 1)
    dp[0] = 1

    for i in lis:
        for j in nextDiv(i):
            dp[j] += dp[j - 1]

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
