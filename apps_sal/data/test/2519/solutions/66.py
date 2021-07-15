#!/usr/bin/env python3
def main():
    import numpy as np

    N, K = list(map(int, input().split()))
    P = np.array(input().split(), np.int32)

    P[:] += 1
    Pcum = np.zeros(N + 1, np.int32)
    Pcum[1:] = np.cumsum(P)
    length_K_sums = Pcum[K:] - Pcum[:-K]
    print((length_K_sums.max() / 2))


def __starting_point():
    main()

__starting_point()
