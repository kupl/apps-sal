def main():
    import sys
    import numpy as np
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    (N, S) = [int(x) for x in input().strip().split()]
    An = [int(x) for x in input().strip().split()]
    dp = np.zeros(S + 1, dtype=int)
    dp[0] = 2
    if An[0] <= S:
        dp[An[0]] = 1
    for n in range(1, N):
        dp *= 2
        dp[An[n]:] += dp[:-An[n]] // 2
        dp %= 998244353
    print(dp[S])


def __starting_point():
    main()


__starting_point()
