#!/usr/bin/env python3
def main():
    import numpy as np

    N = int(input())

    cnt = np.zeros((10, 10), dtype=np.int64)
    for n in [str(x) for x in range(1, N + 1)]:
        cnt[int(n[0])][int(n[-1])] += 1

    print(((cnt[:, :] * cnt.T[:, :]).sum()))


def __starting_point():
    main()


__starting_point()
