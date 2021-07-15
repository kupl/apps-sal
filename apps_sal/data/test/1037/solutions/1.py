def solve(N, A):
    a = [(i, ai) for i, ai in enumerate(A)]
    a.sort(key=lambda x: x[1], reverse=True)

    # import numpy as np
    # dp = np.zeros((N+1, N+1), np.int8)

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    dp[0][0] = 0
    for i, ai in enumerate(a):
        for l in range(i+1):
            r = i - l
            dp[i+1][l] = max(dp[i+1][l], dp[i][l] + ai[1] * ((N-1-r) - ai[0]))
            dp[i+1][l+1] = max(dp[i+1][l+1], dp[i][l] + ai[1] * (ai[0] - l))

    print((max(dp[N])))

def __starting_point():
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)

__starting_point()
