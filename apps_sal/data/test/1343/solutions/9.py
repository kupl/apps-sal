#!/usr/bin/env python3.5
import sys
import heapq


def add_edge(edges, a, b, c):
    edges.append((a, b, c))


def read_graph():
    n, m, k = list(map(int, next(sys.stdin).split()))
    edges = []
    for _ in range(m):
        a, b, c = list(map(int, next(sys.stdin).split()))
        add_edge(edges, a, b, c)
        add_edge(edges, b, a, c)
    stores = set(list(map(int, next(sys.stdin).split())) if k > 0 else [])
    return edges, stores


def solve(edges, stores):
    best = None
    for a, b, c in edges:
        if (
            a in stores and b not in stores
            or b in stores and a not in stores
        ): 
            if best is None or c < best:
                best = c
    return best


def __starting_point():
    edges, stores = read_graph()
    ans = solve(edges, stores)
    print(ans or -1)

__starting_point()
