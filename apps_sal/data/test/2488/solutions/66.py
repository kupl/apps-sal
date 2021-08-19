#!/usr/bin/env python3

from math import ceil
import heapq


def main():
    n, d, a = list(map(int, input().split()))
    q = []
    for i in range(n):
        x, h = list(map(int, input().split()))
        heapq.heappush(q, (x, 0, ceil(h / a)))
    bomb = 0
    res = 0
    while q:
        x, ty, h = heapq.heappop(q)
        if ty == 0:
            if h > bomb:
                heapq.heappush(q, (x + 2 * d, 1, h - bomb))
                res += h - bomb
                bomb = h
        else:
            bomb -= h
    print(res)


def __starting_point():
    main()


__starting_point()
