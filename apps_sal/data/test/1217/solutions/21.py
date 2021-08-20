"""
Codeforces Educational Round 2

Problem 600 B.

@author yamaton
@date 2015-11-30
"""
import bisect


def solve(xs, ys, n, m):
    xs.sort()
    return [bisect.bisect_right(xs, y) for y in ys]


def main():
    (n, m) = list(map(int, input().split()))
    xs = [int(c) for c in input().split()]
    ys = [int(c) for c in input().split()]
    assert len(xs) == n
    assert len(ys) == m
    result = solve(xs, ys, n, m)
    print(*result)


def __starting_point():
    main()


__starting_point()
