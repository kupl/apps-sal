import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T, *AB = list(map(int, read().split()))
    D = [(a, b) for a, b in zip(*[iter(AB)] * 2)]

    D.sort()

    dp = [0] * T
    ans = 0

    for i, (a, b) in enumerate(D[:-1]):
        for t in range(T - 1, a - 1, -1):
            if dp[t] < dp[t - a] + b:
                dp[t] = dp[t - a] + b
        if ans < dp[T - 1] + D[i + 1][1]:
            ans = dp[T - 1] + D[i + 1][1]

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
