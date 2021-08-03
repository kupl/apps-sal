# if graph problem, dont forget to write sys.setrecursionlimit(10**7)
from math import ceil, floor


def solve():

    n, x = list(map(int, input().split()))
    if (1 <= n <= 2):
        print(1)
    else:
        print(ceil((n - 2) / x) + 1)
    return


def main():
    T = int(input())
    for i in range(T):
        solve()
    return


def __starting_point():
    main()


__starting_point()
