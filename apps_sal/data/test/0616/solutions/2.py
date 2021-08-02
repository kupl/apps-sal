def main():
    n, m = tuple([int(t)for t in input().split()])

    keys = []

    dp = [10**9] * (1 << n)
    dp[0] = 0
    for _ in range(m):
        a, _ = tuple([int(t)for t in input().split()])
        c = tuple([int(t)for t in input().split()])
        key = 0
        for c_i in c:
            key |= 1 << (c_i - 1)
        keys.append((a, key))

    for a, key in keys:
        for i in range(1 << n):
            dp[i | key] = min(dp[i | key], dp[i] + a)

    if dp[-1] == 10**9:
        print(-1)
    else:
        print(dp[-1])


def __starting_point():
    main()


__starting_point()
