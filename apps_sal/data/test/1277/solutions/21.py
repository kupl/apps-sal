import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import decimal
import queue


sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))


def main():
    n, u, v = ns()
    edge = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = ns()
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    dist_takahashi = [-1] * n
    dist_aoki = [-1] * n

    def bfs(pos, dist):
        que = queue.Queue()
        que.put(pos)
        dist[pos] = 0

        while not que.empty():
            current = que.get()
            for e in edge[current]:
                if dist[e] == -1:
                    dist[e] = dist[current] + 1
                    que.put(e)

        return dist

    dist_takahashi = bfs(u - 1, dist_takahashi)
    dist_aoki = bfs(v - 1, dist_aoki)

    ans = 0
    for dt, da in zip(dist_takahashi, dist_aoki):
        if dt < da:
            ans = max(ans, da - 1)

    print(ans)


def __starting_point():
    main()


__starting_point()
