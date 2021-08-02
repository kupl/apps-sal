import math
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    s = input().rstrip()
    opt = [[[[math.inf for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
    # opt[x][y][a][b] - x-y counter, transition from a to b
    pairs = [[0 for _ in range(10)] for _ in range(10)]
    for x in range(10):
        for y in range(10):
            for a in range(10):
                for cntx in range(10):
                    for cnty in range(10):
                        dig = (a + cntx * x + cnty * y) % 10
                        if cntx + cnty > 0:
                            opt[x][y][a][dig] = min(opt[x][y][a][dig], cntx + cnty)
    for i in range(1, len(s)):
        pairs[int(s[i - 1])][int(s[i])] += 1

    res = [[0 for _ in range(10)] for _ in range(10)]
    for x in range(10):
        for y in range(10):
            for p1 in range(10):
                for p2 in range(10):
                    p = pairs[p1][p2]
                    if p > 0:
                        if opt[x][y][p1][p2] == math.inf:
                            res[x][y] = -1
                        elif res[x][y] != -1:
                            res[x][y] += p * (opt[x][y][p1][p2] - 1)

    for x in range(10):
        print(*res[x])


def __starting_point():
    main()


__starting_point()
