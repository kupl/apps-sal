import math
import random


def read_ints():
    return [int(x) for x in input(' ').split()]


def main():
    (n,) = read_ints()
    A = [(int(x), i) for (i, x) in enumerate(input(' ').split())]
    A.sort()
    A.append((10 ** 10, n))
    (max_id, max_len, max_last) = (-1, -1, -1)
    (curr_id, curr_len, curr_last) = (-1, -1, -1)
    for (a, i) in A:
        if a == curr_id:
            (curr_len, curr_last) = (curr_len + 1, i)
        else:
            if curr_len >= max_len:
                if curr_len > max_len or curr_last < max_last:
                    (max_id, max_len, max_last) = (curr_id, curr_len, curr_last)
            (curr_id, curr_len, curr_last) = (a, 1, i)
    print(max_id)


def __starting_point():
    main()


__starting_point()
