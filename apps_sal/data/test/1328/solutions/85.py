def main():
    (N, Ma, Mb) = map(int, input().split())
    yakuhin = []
    for i in range(N):
        yakuhin.append(list(map(int, input().split())))
    INF = 10 ** 15
    DP = [[[INF for _ in range(401)] for _ in range(401)] for _ in range(N + 1)]
    DP[0][0][0] = 0
    for i in range(N):
        for j in range(401):
            for k in range(401):
                if DP[i][j][k] != INF:
                    DP[i + 1][j][k] = min(DP[i + 1][j][k], DP[i][j][k])
                    DP[i + 1][j + yakuhin[i][0]][k + yakuhin[i][1]] = min(DP[i + 1][j + yakuhin[i][0]][k + yakuhin[i][1]], DP[i][j][k] + yakuhin[i][2])
    ans = INF
    for i in range(1, N + 1):
        for j in range(1, 401):
            for k in range(1, 401):
                if j * Mb == k * Ma:
                    ans = min(ans, DP[i][j][k])
    print(ans if ans != INF else -1)


main()
