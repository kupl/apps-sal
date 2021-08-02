import numpy as np
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n, k = list(map(int, input().split()))
    p = np.array(read().split(), np.int32)
    p += 1
    pcum = np.zeros(n + 1, np.int32)
    pcum[1:] = p.cumsum()
    sum_k = pcum[k:] - pcum[:-k]
    print((sum_k.max() / 2))


def __starting_point():
    main()


__starting_point()
