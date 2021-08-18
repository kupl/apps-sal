

import math
import sys


def solve(r, w):
    """
    :param r:
    :param w:
    :return:
    """
    num_pairs = int(r.readline())
    pairs = []
    for _ in range(num_pairs):
        line_data = [int(v) for v in r.readline().split()]
        pairs.append((line_data[0], line_data[1],))

        num_1 = line_data[0]
        num_2 = line_data[1]
        ops = 0

        while num_1 > 0 and num_2 > 0:
            if num_1 > num_2:
                num_1, num_2 = num_2, num_1
            ops += num_2 // num_1
            num_2 %= num_1

        print(ops)


def __starting_point():
    solve(sys.stdin, sys.stdout)


__starting_point()
