import numpy as np


def main():
    k, q = [int(x) for x in input().split()]
    d = np.fromstring(input(), np.int64, sep=' ')

    def solve1(d, n):
        zero = np.where(d == 0)[0]
        n_zero = zero.shape[0] * ((n - 1) // k)
        n_zero += np.count_nonzero(zero < (n - 1) % k)
        return n_zero

    def solve2(d, n, x, m):
        a_max = np.sum(d) * ((n - 1) // k) + np.sum(d[:(n - 1) % k])
        return (a_max + x) // m - x // m

    for _ in range(q):
        n, x, m = [int(x) for x in input().split()]
        dm = d % m
        n_zero = solve1(dm, n)
        n_dec = solve2(dm, n, x, m)
        print(n - 1 - n_zero - n_dec)


def __starting_point():
    main()


__starting_point()
