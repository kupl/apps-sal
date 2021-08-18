def sumGCD(N, K, M):
    dp = [None for _ in range(K + 1)]
    for i in reversed(list(range(1, K + 1))):
        dp[i] = pow(K // i, N, M)
        for j in range(2, K // i + 1):
            dp[i] -= dp[i * j]
            dp[i] %= M

    output = 0
    for i in range(1, K + 1):
        output += (dp[i] * i)
        output %= M

    return output


def main():
    N, K = list(map(int, input().split()))

    print((sumGCD(N, K, 10**9 + 7)))


def __starting_point():
    main()


__starting_point()
