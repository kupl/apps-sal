INF = float('inf')


def main():
    n = list(map(int, list(input())))
    n.reverse()
    n.append(0)
    N = len(n) - 1
    DP = [[INF, INF] for i in range(N + 2)]
    DP[-1][1] = 0
    for i in range(N + 1):
        DP[i][0] = min(DP[i - 1][0] + (9 - n[i]), DP[i - 1][1] + (10 - n[i]))
        DP[i][1] = min(DP[i - 1][0] + n[i] + 1, DP[i - 1][1] + n[i])
    ans = min(DP[-2])
    print(ans)


def __starting_point():
    main()


__starting_point()
