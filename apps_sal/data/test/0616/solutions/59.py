def main():
    n, m = map(int, input().split())
    a = [0] * m
    c = [0] * m
    INF = 10**9
    dp = [INF] * 2**n
    for i in range(m):
        a[i] = int(input().split()[0])
        c[i] = sum([1 << (int(i) - 1) for i in input().split()])
    dp[0] = 0
    for i in range(2**n):
        for cos, pat in zip(a, c):
            npat = i | pat
            if dp[npat] > cos + dp[i]:
                dp[npat] = cos + dp[i]
    if dp[2**n - 1] == INF:
        print(-1)
    else:
        print(dp[2**n - 1])


def __starting_point():
    main()


__starting_point()
