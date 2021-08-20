import sys
from bisect import bisect_right


def upgrade_minCost(n, m, antennas):
    covered = [False] * (m + 1)
    intervals = []
    for (x, s) in antennas:
        L = max(1, x - s)
        R = min(m, x + s)
        intervals.append((L, R))
        for i in range(L, R + 1):
            covered[i] = True
    intervals.sort()
    d = [m - i for i in range(m + 1)]
    for i in range(m - 1, -1, -1):
        if covered[i + 1]:
            d[i] = d[i + 1]
        else:
            ant_idx = bisect_right(intervals, (i, m))
            for (L, R) in intervals[ant_idx:]:
                u = L - i - 1
                prev = min(m, R + u)
                d[i] = min(d[i], u + d[prev])
    return d[0]


def main():
    reader = (map(int, s.split()) for s in sys.stdin)
    (n, m) = next(reader)
    antennas = [list(next(reader)) for _ in range(n)]
    ans = upgrade_minCost(n, m, antennas)
    print(ans)


def __starting_point():
    main()


__starting_point()
