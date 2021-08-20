import os
import sys


def main():
    (N, M) = list(map(int, input().split()))
    para0 = (1900 * M + 100 * (N - M)) / 2 ** M
    para1 = 1 - 1 / 2 ** M
    para0_ = para0
    para1_ = 1 / (1 - para1) ** 2
    print(int(para0_ * para1_))


def __starting_point():
    main()


__starting_point()
