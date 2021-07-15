import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    amt = [1]
    a = 6
    while a <= N:
        amt.append(a)
        a *= 6
    a = 9
    while a <= N:
        amt.append(a)
        a *= 9

    dp = [INF] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in amt:
            if i >= a and dp[i] > dp[i - a]:
                dp[i] = dp[i - a] + 1

    print((dp[N]))

    return


def __starting_point():
    main()

__starting_point()
