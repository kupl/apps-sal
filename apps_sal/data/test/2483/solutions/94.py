import sys
import numpy as np
readline = sys.stdin.readline
read = sys.stdin.read


def main():
    (n, c) = map(int, readline().split())
    m = 2 * 10 ** 5
    stc = [list(map(int, l.split())) for l in read().splitlines()]
    cht = np.zeros((c, m + 1), dtype='int64')
    for e in stc:
        cht[e[2] - 1, 2 * e[0] - 1:2 * e[1]] = np.ones(2 * e[1] - 2 * e[0] + 1)
    print(max(np.sum(cht, axis=0)))


def __starting_point():
    main()


__starting_point()
