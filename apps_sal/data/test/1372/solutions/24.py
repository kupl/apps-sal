import sys
import numpy as np


def main():
    (h, n) = list(map(int, sys.stdin.buffer.readline().split()))
    ab = np.fromstring(sys.stdin.buffer.read(), dtype=np.int64, sep=' ')
    a = ab[::2]
    b = ab[1::2]
    amax = a.max()
    dp = np.zeros(h + amax + 1, np.int64)
    for i in range(amax + 1, len(dp)):
        dp[i] = np.min(dp[i - a] + b)
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
