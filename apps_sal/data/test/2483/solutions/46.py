import numpy as np
import sys
input = sys.stdin.readline


def main(args):
    (N, C) = map(int, input().split())
    time = [[0] * (10 ** 5 + 1) for _ in range(C)]
    for _ in range(N):
        (s, t, c) = map(lambda x: int(x) - 1, input().split())
        time[c - 1][s] += 1
        time[c - 1][t + 1] -= 1
    recorder = np.where(np.cumsum(time[0]) > 0, 1, 0)
    for i in range(1, C):
        recorder += np.where(np.cumsum(time[i]) > 0, 1, 0)
    print(max(recorder))


def __starting_point():
    main(sys.argv[1:])


__starting_point()
