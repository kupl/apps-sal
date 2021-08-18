from sys import stdin
import numpy as np


def main():
    readline = stdin.readline
    n, m = map(int, readline().split())
    A = np.array([list(map(int, readline().split())) for _ in range(n)], dtype="int64")

    ans = -float("inf")
    for i in (-1, 1):
        for j in (-1, 1):
            for k in (-1, 1):
                B = np.array([i, j, k], dtype="int64")
                res = np.sort(np.dot(A, B))[::-1][:m].sum()
                ans = max(ans, res)

    print(ans)


def __starting_point():
    main()


__starting_point()
