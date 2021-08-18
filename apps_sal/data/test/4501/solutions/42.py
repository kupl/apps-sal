def abc044_c():
    import numpy as np
    n, a = map(int, input().split())
    x = list(map(lambda x: int(x) - a, input().split()))
    x = np.array(x, dtype=np.int64)

    vrange = n * (a + np.max(x))
    dp = np.zeros((n + 1, 2 * vrange + 1), dtype=np.int64)
    dp[0, vrange] = 1

    for i in np.arange(n):
        dp[i + 1, :] += dp[i, :]
        if 0 < x[i]:
            dp[i + 1, x[i]:] += dp[i, :-x[i]]
        elif x[i] < 0:
            dp[i + 1, :x[i]] += dp[i, -x[i]:]
        else:
            dp[i + 1, :] += dp[i, :]

    ans = dp[n, vrange] - 1
    print(ans)


def __starting_point():
    abc044_c()


__starting_point()
