from sys import stdin
from itertools import accumulate


def main():
    readline = stdin.readline
    n, m = map(int, readline().split())
    a = list(map(int, readline().split()))

    d = dict()
    for s in accumulate(a):
        x = s % m
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    if 0 in d:
        ans = d[0]
    else:
        ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2

    print(ans)


def __starting_point():
    main()


__starting_point()
