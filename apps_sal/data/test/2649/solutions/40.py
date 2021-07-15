"""AtCoder Beginner Contest 178.

E
"""

import sys


def input() -> str:  # noqa: A001
    """Input."""
    return sys.stdin.readline()[:-1]


def calc(p1: list, p2: list) -> int:
    """Calc Manhattan Distance."""
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])


def main():
    """Run."""
    n = int(input())

    patterns = {
        'lt': (1, 1),
        'rt': (-1, 1),
        'lb': (-1, -1),
        'rb': (1, -1),
    }

    points: dict = {k: None for k in list(patterns.keys())}

    for _ in range(n):
        p = list(map(int, input().split(' ')))

        for k, (x, y) in list(patterns.items()):
            max_p = points[k]

            if max_p:
                max_p_pos = (max_p[0] * x) + (max_p[1] * y)
                p_pos = (p[0] * x) + (p[1] * y)
                if max_p_pos < p_pos:
                    points[k] = p
            else:
                points[k] = p

    ans = 0
    for i, p1 in enumerate(points.values()):
        for p2 in list(points.values())[i + 1:]:
            ans = max(ans, calc(p1, p2))

    print(ans)


main()

