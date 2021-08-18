def main():
    n, m = map(int, input().split())
    inf = 10**9
    dp = [inf] * (1 << n)
    dp[0] = 0

    for i in range(m):
        a, b = map(int, input().split())
        c = [1 << (int(x) - 1) for x in input().split()]
        t = sum(c)
        for s in range(1 << n):
            if dp[t | s] > dp[s] + a:
                dp[t | s] = dp[s] + a

    """
  dp=[inf]*(1<<n)
  dp[0]=0
  for s in range(1<<n):
    for bit,c in cost:
      dp[s|bit]=min(dp[s|bit], dp[s]+c)
  """
    print(-1 if dp[-1] == inf else dp[-1])


def __starting_point():
    main()


__starting_point()
