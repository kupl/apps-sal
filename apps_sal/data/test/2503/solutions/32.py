import sys
import numpy as np
read = sys.stdin.read
readline = sys.stdin.readline


def main():
    wb = {'W': 1, 'B': 0}
    (n, k) = list(map(int, readline().split()))
    xyc = [l.split() for l in read().splitlines()]
    xy = [[int(lst[0]) % (2 * k), (int(lst[1]) + k * wb[lst[2]]) % (2 * k)] for lst in xyc]
    mat = np.zeros((k + 1, 2 * k + 1), dtype='int64')
    cand = np.zeros((k + 1, k + 1), dtype='int64')
    for e in xy:
        f0 = e[0] >= k
        f1 = e[1] >= k
        mat[e[0] - f0 * k + 1, e[1] + (-1) ** f1 * f0 * k + 1] += 1
    mat = np.cumsum(mat, axis=0)
    mat = np.cumsum(mat, axis=1)
    cand = mat[k, 2 * k] - mat[k, k:2 * k + 1] + mat[k, :k + 1] - np.reshape(mat[:k + 1, 2 * k], (k + 1, 1)) + 2 * mat[:, k:2 * k + 1] - 2 * mat[:, :k + 1]
    print(max(np.max(cand), mat[k, 2 * k] - np.min(cand)))


def __starting_point():
    main()


__starting_point()
