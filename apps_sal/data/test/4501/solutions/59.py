import sys


def main():
    mod = 1000000007
    inf = float('inf')
    sys.setrecursionlimit(10 ** 6)

    def input():
        return sys.stdin.readline().rstrip()

    def ii():
        return int(input())

    def mi():
        return list(map(int, input().split()))

    def mi_0():
        return [int(x) - 1 for x in input().split()]

    def lmi():
        return list(map(int, input().split()))

    def lmi_0():
        return list([int(x) - 1 for x in input().split()])

    def li():
        return list(input())
    (n, a) = mi()
    L = lmi()
    diff = [elm - a for elm in L]
    dp = [[0] * 5001 for _ in range(n + 1)]
    dp[0][2500] = 1
    for i in range(n):
        for j in range(5001):
            if dp[i][j]:
                dp[i + 1][j + diff[i]] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
    print(dp[n][2500] - 1)


def __starting_point():
    main()


__starting_point()
