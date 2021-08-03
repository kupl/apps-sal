import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b, c = map(int, readline().split())
        G[a - 1].append((b - 1, c))
        G[b - 1].append((a - 1, c))

    Q, K, *XY = map(int, read().split())
    K -= 1

    stack = deque([K])
    dist = [INF] * N
    dist[K] = 0
    while stack:
        v = stack.pop()
        for nv, cost in G[v]:
            if dist[nv] == INF:
                dist[nv] = dist[v] + cost
                stack.append(nv)

    ans = [0] * Q
    for i, (x, y) in enumerate(zip(*[iter(XY)] * 2)):
        ans[i] = dist[x - 1] + dist[y - 1]

    print(*ans, sep='\n')
    return


def __starting_point():
    main()


__starting_point()
