import sys

input = sys.stdin.readline


def main():
    N, M = list(map(int, input().split()))
    A = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], _ = list(map(int, input().split()))
        C[i] = sum(2 ** (int(c) - 1) for c in input().split())

    INF = 10 ** 18
    dp = [INF] * (2 ** N)
    dp[0] = 0
    for a, c in zip(A, C):
        for s in range(2 ** N):
            dp[s | c] = min(dp[s | c], dp[s] + a)

    ans = dp[-1] if dp[-1] != INF else -1
    print(ans)


def __starting_point():
    main()


__starting_point()
