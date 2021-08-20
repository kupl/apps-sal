def main():
    (N, Ma, Mb) = map(int, input().split())
    yakuhin = []
    sa = 0
    sb = 0
    for i in range(N):
        yakuhin.append(list(map(int, input().split())))
        sa += yakuhin[i][0]
        sb += yakuhin[i][1]
    INF = 10 ** 15
    DP = [[[INF for _ in range(sb + 1)] for _ in range(sa + 1)] for _ in range(N + 1)]
    for i in range(N):
        DP[i][0][0] = 0
    for i in range(N):
        for j in range(sa + 1):
            for k in range(sb + 1):
                if j >= yakuhin[i][0] and k >= yakuhin[i][1]:
                    DP[i + 1][j][k] = min(DP[i][j][k], DP[i][j - yakuhin[i][0]][k - yakuhin[i][1]] + yakuhin[i][2])
                else:
                    DP[i + 1][j][k] = min(DP[i + 1][j][k], DP[i][j][k])
    ans = INF
    for i in range(1, N + 1):
        for j in range(1, sa + 1):
            for k in range(1, sb + 1):
                if j * Mb == k * Ma:
                    ans = min(ans, DP[i][j][k])
    print(ans if ans != INF else -1)


main()
