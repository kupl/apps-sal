"""
Codeforces Round #361 (Div. 2)

Problem 689 B. Mike and Shortcuts

@author yamaton
@date 2016-07-09
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, n):
    nodes = list(range(1, n + 1))

    neighbors = collections.defaultdict(set)
    for from_, to_ in zip(nodes, nodes[1:]):
        neighbors[from_].add(to_)
        neighbors[to_].add(from_)
    for from_, to_ in enumerate(xs, 1):
        neighbors[from_].add(to_)

    distance = {1: 0}
    q = collections.deque([1])
    while q:
        node = q.popleft()
        for x in neighbors[node]:
            if x not in distance:
                distance[x] = distance[node] + 1
                q.append(x)
    return [distance[i] for i in nodes]


def pp(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    n = int(input())
    xs = [int(s) for s in input().strip().split()]
    assert len(xs) == n
    result = solve(xs, n)
    print(*result)


def __starting_point():
    main()


__starting_point()
