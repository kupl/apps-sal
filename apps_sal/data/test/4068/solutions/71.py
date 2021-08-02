def solve(N, a):
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    step = [0] * (N + 1)
    for aa in a:
        step[aa] = 1

    dp[0] = 1
    if step[1] == 0:
        dp[1] = 1

    for i in range(2, N + 1):
        if step[i] == 0:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= mod

    return dp[N]


def __starting_point():
    N, M = list(map(int, input().split()))
    a = [int(input()) for _ in range(M)]

    print((solve(N, a)))


__starting_point()
