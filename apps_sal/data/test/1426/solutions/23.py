from collections import deque


def main():

    n, m = map(int, input().split())
    INF = 10**9
    d = [[INF] * 3 for i in range(n)]
    to = [[] for i in range(n)]
    for i in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        to[u].append(v)
    s, t = map(lambda x: int(x) - 1, input().split())

    # print(to)
    # calc d (after 3 times dist)
    d[s][0] = 0
    cnt = 0
    q = deque([(s, cnt)])
    while q:
        u, c = q.popleft()
        for v in to[u]:
            nc = (c + 1) % 3
            if d[v][nc] != INF:
                continue
            d[v][nc] = d[u][c] + 1
            q.append((v, nc))

    # print(d)
    ans = d[t][0]
    print(ans // 3 if ans != INF else -1)


def __starting_point():
    main()


__starting_point()
