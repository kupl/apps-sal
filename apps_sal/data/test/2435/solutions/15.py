#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, m = map(int, input().split())
    x -= 1
    minima = x
    maxima = x
    for _ in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if r >= minima:
            minima = min(l, minima)
        if l <= maxima:
            maxima = max(r, maxima)
    print(maxima - minima + 1)
