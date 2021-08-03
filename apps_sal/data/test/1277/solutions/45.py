import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, ta, ao, *AB = list(map(int, read().split()))
    ta -= 1
    ao -= 1

    G = [[] for _ in range(N)]
    for a, b in zip(*[iter(AB)] * 2):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    dist_ta = [-1] * N
    dist_ta[ta] = 0
    queue = deque([ta])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if dist_ta[nv] == -1:
                dist_ta[nv] = dist_ta[v] + 1
                queue.append(nv)

    dist_ao = [-1] * N
    dist_ao[ao] = 0
    queue = deque([ao])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if dist_ao[nv] == -1:
                dist_ao[nv] = dist_ao[v] + 1
                queue.append(nv)

    d_ao = 0
    for d1, d2 in zip(dist_ta, dist_ao):
        if d1 < d2 and d_ao < d2:
            d_ao = d2

    if d_ao == 0:
        if dist_ta[ao] == 1:
            print((0))
        else:
            print((1))

    print((d_ao - 1))
    return


def __starting_point():
    main()


__starting_point()
