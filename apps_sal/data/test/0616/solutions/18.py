def main():
    (n, m) = map(int, input().split())
    costs = [None] * m
    keys = [None] * m
    pattern = 2 ** n
    inf = 10 ** 12
    dp = [inf] * pattern
    for i in range(m):
        costs[i] = int(input().split()[0])
        keys[i] = sum([1 << int(i) - 1 for i in input().split()])
    dp[0] = 0
    for i in range(pattern):
        for (cost, key) in zip(costs, keys):
            pi = i | key
            if dp[pi] > cost + dp[i]:
                dp[pi] = cost + dp[i]
    if dp[pattern - 1] == inf:
        print(-1)
    else:
        print(dp[pattern - 1])


def __starting_point():
    main()


__starting_point()
