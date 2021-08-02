def main():
    import numpy as np
    n = int(input())
    a = list(enumerate(map(int, input().split())))
    a.sort(key=lambda x: -x[1])
    dp = [np.zeros(i + 1, dtype=np.int64) for i in range(n + 1)]
    dp[0] = np.zeros(1, dtype=np.int64)
    r = np.arange(n + 1, dtype=np.int64)
    for time, ix in enumerate(a):
        i, x = ix
        dp[time + 1][1:] = dp[time][:time + 1] + (i - r[:time + 1]) * x
        np.maximum(dp[time + 1][:-1], dp[time] + ((n - 1 - (time - r[:time + 1])) - i) * x, out=dp[time + 1][:-1])
    print(np.max(dp[n]))


main()
