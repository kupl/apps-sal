import math
from collections import defaultdict
import sys


def main():
    n, m, k = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for i in range(n):
        g[i] = list(map(int, input().split()))

    cnt = [[defaultdict(int) for _ in range(m)] for _ in range(n)]

    all = n + m - 2
    half = all // 2
    res = [0]

    def go_start(x, y, val, steps):
        val ^= g[x][y]
        if steps == half:
            cnt[x][y][val] += 1
            return

        if x + 1 < n:
            go_start(x + 1, y, val, steps + 1)

        if y + 1 < m:
            go_start(x, y + 1, val, steps + 1)

    def go_end(x, y, val, steps):
        if steps + half == all:
            comp = k ^ val
            if comp in cnt[x][y]:
                res[0] += cnt[x][y][comp]
            return

        val ^= g[x][y]

        if x > 0:
            go_end(x - 1, y, val, steps + 1)
        if y > 0:
            go_end(x, y - 1, val, steps + 1)

    go_start(0, 0, 0, 0)
    go_end(n - 1, m - 1, 0, 0)

    print(res[0])


def __starting_point():
    main()


__starting_point()
