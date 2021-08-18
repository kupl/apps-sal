

from collections import deque


def main():
    n = int(input())
    neis = [[] for i in range(n + 1)]
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        neis[u].append(v)
        neis[v].append(u)

    def fake_dfs(start_point):
        nonlocal neis

        vis = [0 for i in range(n + 1)]
        nodes = [1 for i in range(n + 1)]
        pre = [None for i in range(n + 1)]
        cut = 0

        q = deque()
        q.append(start_point)
        pre[start_point] = start_point

        while len(q) > 0:
            top = q[-1]

            if vis[top] < len(neis[top]):
                nei = neis[top][vis[top]]
                vis[top] += 1
                if nei != pre[top]:
                    q.append(nei)
                    pre[nei] = top
            else:
                if top != start_point:
                    nodes[pre[top]] += nodes[top]
                    if nodes[top] & 1 == 0:
                        cut += 1
                q.pop()

        if nodes[1] & 1 == 0:
            print(cut)
        else:
            print(-1)

    fake_dfs(1)


def __starting_point():
    main()


__starting_point()
