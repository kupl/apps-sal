from sys import stdin, stdout  # only need for big input
from itertools import permutations


def read_int_from_line():
    return list(map(int, input().split()))


def solve():
    n, k = read_int_from_line()
    a = read_int_from_line()
    if (n - 1) % (k - 1) == 0:
        ans = (n - 1) // (k - 1)
    else:
        ans = (n - 1) // (k - 1) + 1
    print(ans)


def main():
    solve()


def __starting_point():
    main()


__starting_point()
