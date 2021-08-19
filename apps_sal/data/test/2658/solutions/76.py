import sys
import numpy as np


def input():
    return sys.stdin.readline().rstrip()


def main():
    (n, k) = list(map(int, input().split()))
    warps = list(map(int, input().split()))
    warps = [0] + warps
    warps = np.array(warps, dtype=int)
    dp = np.zeros((k.bit_length() + 1, n + 1), dtype=int)
    dp[0, :] = warps
    for h in range(1, len(dp)):
        dp[h] = dp[h - 1][dp[h - 1]]
    node = 1
    for i in range(k.bit_length(), -1, -1):
        if k >> i & 1:
            node = dp[i][node]
    print(node)


main()
