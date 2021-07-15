def main():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [0] * N
    for i in range(1, N):
        h = A[i - 1] - A[i]
        if h > 0:
            A[i] += h
            dp[i] = dp[i-1] + h
        else:
            dp[i] = dp[i-1]

    print((dp[-1]))
    return


def __starting_point():
    main()

__starting_point()
