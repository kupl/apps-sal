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

    # dp[i][l][r]
    # 大きい方からi個まで左右を決めて
    # 左をl回、右をr回使ったときの最大値
    # r = i - l
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        ai, pi = AP[i]
        for l in range(i + 1):
            r = i - l
            # 左
            if dp[i + 1][l + 1] < dp[i][l] + (pi - l) * ai:
                dp[i + 1][l + 1] = dp[i][l] + (pi - l) * ai
            # 右
            if dp[i + 1][l] < dp[i][l] + ((N - r - 1) - pi) * ai:
                dp[i + 1][l] = dp[i][l] + ((N - r - 1) - pi) * ai

    print(max(dp[N]))


main()
