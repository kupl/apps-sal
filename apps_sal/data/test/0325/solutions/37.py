import sys
from collections import deque
read = sys.stdin.read
INF = 1 << 60


def main():
    (N, M, P, *ABC) = list(map(int, read().split()))
    G = [[] for _ in range(N)]
    G_rev = [[] for _ in range(N)]
    edge = []
    for (a, b, c) in zip(*[iter(ABC)] * 3):
        a -= 1
        b -= 1
        c = P - c
        G[a].append(b)
        G_rev[b].append(a)
        edge.append((a, b, c))
    reachable_1 = [False] * N
    reachable_N = [False] * N
    reachable_1[0] = True
    reachable_N[N - 1] = True
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if not reachable_1[nv]:
                reachable_1[nv] = True
                queue.append(nv)
    queue = deque([N - 1])
    while queue:
        v = queue.popleft()
        for nv in G_rev[v]:
            if not reachable_N[nv]:
                reachable_N[nv] = True
                queue.append(nv)
    ok = [reachable_1[i] and reachable_N[i] for i in range(N)]
    dist = [INF] * N
    dist[0] = 0
    for i in range(N):
        for (a, b, c) in edge:
            if not ok[a] or not ok[b]:
                continue
            if dist[b] > dist[a] + c:
                if i < N - 1:
                    dist[b] = dist[a] + c
                else:
                    print(-1)
                    return
    score = -dist[N - 1]
    print(max(score, 0))
    return


def __starting_point():
    main()


__starting_point()
