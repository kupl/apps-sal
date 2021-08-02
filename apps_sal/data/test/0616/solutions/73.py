import sys

input = sys.stdin.readline
INF = float("inf")


def main():
    N, M = list(map(int, input().split()))
    keys = [None] * M
    for i in range(M):
        a, b = list(map(int, input().split()))
        s = 0
        for c in map(int, input().split()):
            c -= 1
            s |= 1 << c
        keys[i] = (s, a)

    dp = [INF] * (2 ** N)
    dp[0] = 0
    for s in range(2 ** N):
        for key, a in keys:
            t = s | key
            dp[t] = min(dp[t], dp[s] + a)

    ans = dp[-1] if dp[-1] != INF else -1
    print(ans)


def __starting_point():
    main()


__starting_point()
