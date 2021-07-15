3

import array
import math
import os
import random
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, M, G):
    A = {}

    for i in range(N):
        t = frozenset(G[i])
        if t not in A:
            A[t] = set([i])
        else:
            A[t].add(i)

    if len(A) != 3:
        return None

    (a1, v1), (a2, v2), (a3, v3) = A.items()
    v1 = frozenset(v1)
    v2 = frozenset(v2)
    v3 = frozenset(v3)

    if a1 != v2 | v3 or a2 != v3 | v1 or a3 != v1 | v2:
        return None

    ans = [0] * N
    for v in v1:
        ans[v] = 1
    for v in v2:
        ans[v] = 2
    for v in v3:
        ans[v] = 3
    return ans


def main():
    N, M = [int(e) for e in inp().split()]
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) - 1 for e in inp().split()]
        G[a].append(b)
        G[b].append(a)

    ans = solve(N, M, G)
    if not ans:
        print('-1')
    else:
        print(*ans)


def __starting_point():
    main()

__starting_point()
