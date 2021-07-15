#!/usr/bin/env python3

from math import ceil
import heapq

def main():
    n, d, a = list(map(int, input().split()))
    q = []
    for i in range(n):
        x, h = list(map(int, input().split()))
        heapq.heappush(q, (x, -(h // a + (1 if (h % a) else 0))))
    bomb = 0
    res = 0
    while q:
        x, h = heapq.heappop(q)
        if h < 0:
            h *= -1
            if h > bomb:
                heapq.heappush(q, (x + 2 * d, h - bomb))
                res += h - bomb
                bomb = h
        else:
            bomb -= h
    print(res)

def __starting_point():
    main()

__starting_point()
