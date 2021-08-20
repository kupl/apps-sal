def main():
    inf = 10 ** 8 + 1
    (N, M) = list(map(int, input().split()))
    dp = [inf] * (1 << N)
    dp[0] = 0
    for _ in range(M):
        (price, _) = list(map(int, input().split()))
        c = (int(x) - 1 for x in input().split())
        k = sum((1 << x for x in c))
        for bit in reversed(list(range(1 << N))):
            nbit = bit | k
            dp[nbit] = min(dp[nbit], dp[bit] + price)
    ans = dp[(1 << N) - 1]
    if ans == inf:
        print(-1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
