def main():
    from operator import itemgetter
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    AP = []
    for i in range(N):
        AP.append((A[i], i))
    AP.sort(key=itemgetter(0), reverse=True)

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        ai, pi = AP[i]
        for l in range(i + 1):
            r = i - l
            if dp[i + 1][l + 1] < dp[i][l] + (pi - l) * ai:
                dp[i + 1][l + 1] = dp[i][l] + (pi - l) * ai
            if dp[i + 1][l] < dp[i][l] + ((N - r - 1) - pi) * ai:
                dp[i + 1][l] = dp[i][l] + ((N - r - 1) - pi) * ai

    print(max(dp[N]))


main()
