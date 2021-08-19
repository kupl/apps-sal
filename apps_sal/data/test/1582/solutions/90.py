#!/usr/bin/env python3
def main():
    import numpy as np

    N = int(input())

    cnt = np.zeros((10, 10), dtype=np.int64)
    for n in map(str, list(range(1, N + 1))):
        cnt[int(n[0])][int(n[-1])] += 1

    print((np.sum(cnt * cnt.T)))


def __starting_point():
    main()


__starting_point()
