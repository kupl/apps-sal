#!/usr/bin/env python3
def main():
    from itertools import combinations

    _ = int(input())
    d = [int(x) for x in input().split()]

    print((sum([a * b for a, b in combinations(d, 2)])))


def __starting_point():
    main()


__starting_point()
