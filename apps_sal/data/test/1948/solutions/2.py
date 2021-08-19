#!/usr/bin/pypy3

from sys import stdin, stderr
from collections import defaultdict


def readInts(): return map(int, stdin.readline().strip().split())
def print_err(*args, **kwargs): print(*args, file=stderr, **kwargs)


def dfs(n, g, b):
    s = [(1, 0, 1)]
    b_depth = 0
    parents = [None for _ in range(n + 1)]
    while s:
        node, depth, pn = s.pop()
        parents[node] = pn
        if node == b:
            b_depth = depth
            break
        depth += 1
        for nn in g[node]:
            if nn == pn:
                continue
            s.append((nn, depth, node))

    anc_node = b
    for _ in range((b_depth - 1) // 2):
        anc_node = parents[anc_node]
    s = [(1, False, 0, 1)]
    best = 0
    while s:
        node, bd, depth, pn = s.pop()
        bd |= node == anc_node
        if bd and best < depth:
            best = depth
        depth += 1
        for nn in g[node]:
            if nn == pn:
                continue
            s.append((nn, bd, depth, node))
    return best


def run():
    n, x = readInts()
    g = defaultdict(list)
    for _ in range(n - 1):
        a, b = readInts()
        g[a].append(b)
        g[b].append(a)
    print(dfs(n, g, x) * 2)


run()
