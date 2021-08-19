import sys
input = sys.stdin.readline
INF = float('inf')


def main():
    (H, N) = list(map(int, input().split()))
    A = [0] * N
    B = [0] * N
    for i in range(N):
        (A[i], B[i]) = list(map(int, input().split()))
    dp = [INF] * (H + max(A))
    dp[0] = 0
    for h in range(H):
        for (a, b) in zip(A, B):
            if dp[h] + b < dp[h + a]:
                dp[h + a] = dp[h] + b
    ans = min(dp[H:])
    print(ans)


def __starting_point():
    main()


__starting_point()
