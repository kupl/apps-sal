from itertools import *


def main(n, x, l, r):
    s = 0
    curr = 1
    for i in range(n):
        skip = (l[i] - curr) // x
        s += r[i] - curr - skip * x + 1
        curr = r[i] + 1
    print(s)


def main_input(info=0):
    n, x = list(map(int, input().split()))
    l, r = list(range(n)), list(range(n))
    for i in range(n):
        l[i], r[i] = list(map(int, input().split()))
    main(n, x, l, r)


def __starting_point():
    main_input()


__starting_point()
