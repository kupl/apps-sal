def main():
    N, M = list(map(int, input().split()))
    inf = 10**15
    p = 1 << N
    dp = [inf] * p
    dp[0] = 0
    for i in range(M):
        a, b = list(map(int, input().split()))
        c = sum(1 << (i - 1) for i in map(int, input().split()))
        for j in range(p):
            dp[c | j] = min(dp[j] + a, dp[c | j])
    if dp[-1] == inf:
        print((-1))
    else:
        print((int(dp[-1])))


def __starting_point():
    main()


__starting_point()
