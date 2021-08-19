def main():
    (h, n) = list(map(int, input().split()))
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    large_num = 10 ** 9
    dp = [large_num] * (h + 10 ** 4 + 1)
    dp[0] = 0
    for abe in ab:
        a = abe[0]
        b = abe[1]
        for i1 in range(h + 1):
            if dp[i1 + a] > dp[i1] + b:
                dp[i1 + a] = dp[i1] + b
    r = min(dp[h:])
    print(r)


def __starting_point():
    main()


__starting_point()
