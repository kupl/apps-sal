from sys import stdin, stdout
from itertools import permutations


def read_int_from_line():
    return list(map(int, input().split()))


def solve():
    n, m = read_int_from_line()
    if n > m:
        n, m = m, n
    if n == 1:
        if m == 1:
            print(1)
        else:
            print(m - 2)
    else:
        print((n - 2) * (m - 2))


def main():
    solve()


def __starting_point():
    main()


__starting_point()
