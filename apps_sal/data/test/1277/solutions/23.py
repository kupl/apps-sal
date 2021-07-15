import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: list(map(int, readline().split()))
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: list(map(int, read().split()))


def bfs(N, v0, edge):

    search = [-1] * N
    search[v0] = 0
    q = deque()
    q.append(v0)

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if search[nv] == -1:
                q.append(nv)
                search[nv] = search[v] + 1

    return search


def bfs2(N, v0, edge, dis):

    q = deque()
    q.append(v0)

    max_dis = dis[v0]
    while q:
        v = q.popleft()
        for nv in edge[v]:
            if dis[v] < dis[nv]:
                q.append(nv)
                max_dis = max(max_dis, dis[nv])

    return max_dis


def main():

    N, taka, aoki = in_nn()
    taka, aoki = taka - 1, aoki - 1

    edge = [[] for _ in range(N)]
    for i in range(N - 1):
        x, y = in_nn()
        x, y = x - 1, y - 1
        edge[x].append(y)
        edge[y].append(x)

    dis = bfs(N, aoki, edge)

    if dis[taka] > 2:
        x = (dis[taka] + 1) // 2 - 1
        for _ in range(x):
            for v in edge[taka]:
                if dis[v] < dis[taka]:
                    taka = v
                    break

    ans = bfs2(N, taka, edge, dis) - 1
    print(ans)


def __starting_point():
    main()

__starting_point()
