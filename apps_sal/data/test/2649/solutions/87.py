#!/usr/bin/env python3


def main():
    n = int(input())

    ls = []
    for i in range(n):
        p = list(map(int, input().split()))
        np = (p[0] + p[1], p[0] - p[1])
        ls.append(np)

    minx = float("inf")
    miny = float("inf")
    maxx = -float("inf")
    maxy = -float("inf")

    for i in range(len(ls)):
        x, y = ls[i]
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    print((max(maxx - minx, maxy - miny)))


main()


