def min(a, b):
    return a if a <= b else b


def main():
    (n, m) = map(int, input().split())
    inf = 10 ** 9
    cost = [0] * m
    dp = [inf] * (1 << n)
    dp[0] = 0
    for i in range(m):
        (a, b) = map(int, input().split())
        t = sum([1 << int(x) - 1 for x in input().split()])
        for s in range(1 << n):
            dp[t | s] = min(dp[t | s], dp[s] + a)
    print(-1 if dp[-1] == inf else dp[-1])


def __starting_point():
    main()


__starting_point()
