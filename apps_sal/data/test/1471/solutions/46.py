from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


def main():
    n = ii()
    edge = [[] for _ in range(n)]
    for i in range(n - 1):
        (u, v, w) = mi()
        u -= 1
        v -= 1
        edge[u].append((v, w))
        edge[v].append((u, w))
    dist = [0] * n
    parent = [-1] * n
    que = deque([0])
    while que:
        v = que.pop()
        for (nv, nx) in edge[v]:
            if parent[v] == nv:
                continue
            parent[nv] = v
            dist[nv] = dist[v] + nx % 2
            dist[nv] %= 2
            que.append(nv)
    print(*dist, sep='\n')


def __starting_point():
    main()


__starting_point()
