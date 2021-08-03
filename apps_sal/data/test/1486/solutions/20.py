#!/usr/bin/env python3
"""
Codeforces
567 A. Lineland Mail

@author yamaton
@date 2015-08-05
"""

import itertools


def solve(xs):
    mmm = 10000000000
    neighbour_dist = [mmm] + [y - x for (x, y) in zip(xs, xs[1:])] + [mmm]
    min_dists = [min(a, b) for (a, b) in zip(neighbour_dist, neighbour_dist[1:])]
    max_dists = [max(xs[-1] - x, x - xs[0]) for x in xs]
    return list(zip(min_dists, max_dists))


def main():
    n = int(input())
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n
    result = solve(xs)
    for out in result:
        print(' '.join(str(c) for c in out))


def __starting_point():
    main()


__starting_point()
