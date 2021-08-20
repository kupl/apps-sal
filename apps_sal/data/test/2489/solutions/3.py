import numpy as np
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    a = np.array(read().split(), np.int32)[1:]
    count = np.zeros(10 ** 6 + 1, np.int32)
    for ae in a:
        if count[ae] <= 1:
            count[::ae] += 1
    r = 0
    for ae in a:
        r += count[ae] == 1
    print(r)


def __starting_point():
    main()


__starting_point()
