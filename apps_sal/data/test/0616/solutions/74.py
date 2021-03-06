def main():
    (n, m) = map(int, input().split())
    inf = 10 ** 9
    dp = [inf] * (1 << n)
    dp[0] = 0
    for i in range(m):
        (a, b) = map(int, input().split())
        c = [1 << int(x) - 1 for x in input().split()]
        t = sum(c)
        for s in range(1 << n):
            dp[t | s] = min(dp[t | s], dp[s] + a)
    '\n  dp=[inf]*(1<<n)\n  dp[0]=0\n  for s in range(1<<n):\n    for bit,c in cost:\n      dp[s|bit]=min(dp[s|bit], dp[s]+c)\n  #print(dp)\n  '
    print(-1 if dp[-1] == inf else dp[-1])


def __starting_point():
    main()


__starting_point()
