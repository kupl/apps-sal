import numpy as np
import sys
input = sys.stdin.readline


def main():
    h, w, k = list(map(int, input().split()))
    values = np.zeros((h, w), dtype=np.int64)
    items = np.array([list(map(int, input().split())) for _ in range(k)])
    ys, xs, vs = items[:, 0] - 1, items[:, 1] - 1, items[:, 2]
    values[ys, xs] = vs

    DP = np.zeros(w + 1, dtype=np.int64)
    for line in values:
        DP[1:] += line
        DP = np.maximum.accumulate(DP)
        for _ in range(2):
            DP[1:] = np.maximum(DP[:-1] + line, DP[1:])
            DP = np.maximum.accumulate(DP)
    print((DP[-1]))


def __starting_point():
    main()

__starting_point()
