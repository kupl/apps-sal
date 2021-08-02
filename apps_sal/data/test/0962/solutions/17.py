
from collections import deque


def resolve():
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(x) - 1 for x in input().split()]
        G[a].append(b)

    shortest = N + 1
    res = []
    for s in range(N):
        dist = [-1] * N
        pre = [-1] * N
        q = deque()
        q.append(s)
        dist[s] = 0
        while q:
            v = q.popleft()
            for to in G[v]:
                if dist[to] == -1:
                    dist[to] = dist[v] + 1
                    pre[to] = v
                    q.append(to)

        for t in range(N):
            if t == s or dist[t] == -1:
                continue
            for to in G[t]:
                if to == s:  # サイクルになっている頂点
                    tmp = [s]
                    cur = t
                    while cur != s:
                        tmp.append(cur)
                        cur = pre[cur]
                    if shortest > len(tmp):
                        shortest = len(tmp)
                        res = tmp

    if shortest == N + 1:
        print((-1))
    else:
        print((len(res)))
        res.sort()
        for v in res:
            print((v + 1))


def __starting_point():
    resolve()


__starting_point()
