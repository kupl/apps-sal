import sys
from itertools import chain

n, k, *a = map(int, sys.stdin.read().split())
*a, = map(lambda x: min(k, x), a)
a.sort()

mask = (1 << k) - 1


def is_needed(i):
    res = 1
    for j in chain(a[:i], a[i + 1:]):
        res |= res << j
        res &= mask
    return res >> (k - a[i])


def main():
    lo = 0
    hi = n
    while lo != hi:
        i = (lo + hi) // 2
        if is_needed(i):
            hi = i
        else:
            lo = i + 1

    return hi


def __starting_point():
    ans = main()
    print(ans)


__starting_point()
