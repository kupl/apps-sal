from itertools import permutations
import math


def main():
    N = int(input())

    p = []
    for i in range(N):
        p.append(list(map(int, input().split())))

    c = 0
    tot = 0

    for points in permutations(p):
        d = 0
        for i in range(1, len(points)):
            d += dist(points[i - 1], points[i])

        c += 1
        tot += d

    print(tot / c)


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def __starting_point():
    main()


__starting_point()
