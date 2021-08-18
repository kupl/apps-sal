from functools import reduce
from operator import xor
import numpy as np


def main():
    N = int(input())
    A = np.array(input().split(), np.int64)
    A_xor_all = np.bitwise_xor.reduce(A)

    mask = ~A_xor_all
    A_dash = A & mask

    ans = 0
    while True:
        _max = A_dash.max()
        if _max == 0:
            break
        most_left = int(_max).bit_length()
        b = 1 << (most_left - 1)
        A_dash[A_dash & b > 0] ^= _max
        if ans & b == 0:
            ans ^= _max

    print(2 * ans + A_xor_all)


def __starting_point():
    main()


__starting_point()
