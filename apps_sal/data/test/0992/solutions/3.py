def main():
    import sys
    mod = 998244353

    def input():
        return sys.stdin.readline().rstrip()
    (n, s) = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (s + 1)
    dp[0] = 1
    import numpy as np
    dp = np.array(dp)
    for i in range(n):
        dp[a[i]:] = (2 * dp[a[i]:] % mod + dp[:-a[i]]) % mod
        dp[:a[i]] *= 2
        dp[:a[i]] %= mod
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
