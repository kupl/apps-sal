def main():
    n = list(input())
    k = int(input())
    N = len(n)
    for i in range(N):
        n[i] = int(n[i])
    dp1 = [[0 for _ in range(k + 1)] for _ in range(N + 1)]
    dp2 = [[0 for _ in range(k + 1)] for _ in range(N + 1)]
    dp1[0][0] = 1
    for i in range(N):
        for j in range(k + 1):
            dp2[i + 1][j] += dp2[i][j]
            if j < k:
                dp2[i + 1][j + 1] += dp2[i][j] * 9
            if n[i]:
                dp2[i + 1][j] += dp1[i][j]
                if j == k:
                    continue
                dp1[i + 1][j + 1] += dp1[i][j]
                dp2[i + 1][j + 1] += dp1[i][j] * (n[i] - 1)
            else:
                dp1[i + 1][j] += dp1[i][j]
    print(dp1[N][k] + dp2[N][k])


def __starting_point():
    main()


__starting_point()
