import numpy as np
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    h, n = map(int, input().split())
    lis = np.array([list(map(int, input().split())) for _ in range(n)])
    dp = np.zeros(10**4 + 1, int)
    dp[0] = 0
    for i in range(1, h + 1):
        dp[i] = np.min(dp[np.maximum(i - lis[:, 0], 0)] + lis[:, 1])
    print(dp[h])


def __starting_point():
    main()


__starting_point()
