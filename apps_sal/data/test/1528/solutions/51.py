# create date: 2020-07-01 09:01

from functools import lru_cache
import sys
stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))


@lru_cache(maxsize=2**52 - 3)
def f(n, x):
    if n == 0:
        return 1

    if x == 1:
        return 0
    elif x <= 2**(n + 1) - 2:
        #print("f({}, {})".format(n-1, x-1))
        return f(n - 1, x - 1)
    elif x == 2**(n + 1) - 1:
        return f(n - 1, 2**(n + 1) - 3) + 1
    elif x < 2**(n + 2) - 2:
        return f(n - 1, 2**(n + 1) - 3) + 1 + f(n - 1, x - (2**(n + 1) - 1))
    else:
        return 2 * f(n - 1, 2**(n + 1) - 3) + 1


def main():
    n, x = na()
    print(f(n, x))


def __starting_point():
    main()


__starting_point()
