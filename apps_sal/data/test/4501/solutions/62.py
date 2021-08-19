import sys
from collections import defaultdict
(n, a, *x) = map(int, sys.stdin.read().split())
for i in range(n):
    x[i] -= a


def main():
    dp = defaultdict(int)
    dp[0] = 1
    for i in range(n):
        ndp = dp.copy()
        for (k, v) in dp.items():
            ndp[k + x[i]] += v
        dp = ndp
    print(dp[0] - 1)


def __starting_point():
    main()


__starting_point()
