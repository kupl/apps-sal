from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    G_rev = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G_rev[b].append(a)

    s, g = None, None
    ans = INF
    q = deque([])
    for i in range(N):
        q.append(i)
        dist = [-1] * N
        dist[i] = 0
        while q:
            v = q.popleft()
            for e in G[v]:
                if i == e:
                    if ans > dist[v] + 1:
                        ans = dist[v] + 1
                        s, g = i, v
                elif dist[e] < 0:
                    dist[e] = dist[v] + 1
                    q.append(e)

    if ans == INF:
        print(-1)
    else:
        print(ans)
        q.append(s)
        dist = [-1] * N
        dist[s] = 0
        while q:
            v = q.popleft()
            for e in G[v]:
                if e == g:
                    dist[g] = dist[v] + 1
                    q.clear()
                    break
                elif dist[e] < 0:
                    dist[e] = dist[v] + 1
                    q.append(e)
        route = [g + 1]
        now = g
        while now != s:
            for e in G_rev[now]:
                if dist[e] == dist[now] - 1:
                    now = e
                    break
            route.append(now + 1)
        print('\n'.join(map(str, route)))


def __starting_point():
    main()


__starting_point()
