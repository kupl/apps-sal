import sys
import numpy as np


def main():
    input = sys.stdin.readline
    (N, T) = map(int, input().split())
    dishes = []
    for _ in range(N):
        (a, b) = map(int, input().split())
        dishes.append((a, b))
    dishes = sorted(dishes, key=lambda x: x[0])
    ans = 0
    dp = np.zeros(T, dtype=int)
    for (a, b) in dishes:
        ans = max(ans, dp.max() + b)
        np.maximum(dp[:-a] + b, dp[a:], out=dp[a:])
    return ans


def __starting_point():
    print(main())


__starting_point()
