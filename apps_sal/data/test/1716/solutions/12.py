import numpy as np
import sys
input = sys.stdin.readline


def main():
    n, m, q = map(int, input().split())
    counts = np.zeros((n + 1, n + 1), dtype=np.int32)
    for _ in range(m):
        from_, to = map(int, input().split())
        counts[:from_ + 1, to] += 1

    counts = np.cumsum(counts, axis=1)

    queries = np.array([list(map(int, input().split())) for _ in range(q)])
    ps = queries[:, 0]
    qs = queries[:, 1]
    res = counts[ps, qs]
    print(*res, sep="\n")


def __starting_point():
    main()


__starting_point()
