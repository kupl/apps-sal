#!/usr/bin/env python3
from itertools import islice
import math


def squared_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def main():
    n, x1, y1, x2, y2 = list(map(int, input().split()))
    f1, f2 = (x1, y1), (x2, y2)
    flowers = sorted([(int(x), int(y)) for x, y in (input().split() for _ in range(n))],
                     key=lambda x: squared_distance(x, f1), reverse=True)

    ans = squared_distance(f1, flowers[0])

    max_distance_2 = 0

    for i in range(1, n):
        d1 = squared_distance(f1, flowers[i])
        max_distance_2 = max(max_distance_2, squared_distance(f2, flowers[i - 1]))
        ans = min(ans, d1 + max_distance_2)

    max_distance_2 = max(max_distance_2, squared_distance(f2, flowers[-1]))

    ans = min(ans, max_distance_2)

    print(int(ans))


def __starting_point():
    main()


__starting_point()
