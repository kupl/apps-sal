from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N - 1)]
    Q, K = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    to = [[] for _ in range(N)]
    for a, b, c in info:
        a -= 1
        b -= 1
        to[a].append((b, c))
        to[b].append((a, c))

    INF = 10**18
    dist = [INF] * N

    def dfs(s):
        stack = deque()
        push = stack.append
        pop = stack.pop

        dist[s] = 0
        push(s)

        while stack:
            now = pop()
            now_cost = dist[now]

            for nv, c in to[now]:
                if dist[nv] != INF:
                    continue
                dist[nv] = now_cost + c
                push(nv)

    K -= 1
    dfs(K)
    ans = []
    for x, y in queries:
        x -= 1
        y -= 1
        xy = dist[x] + dist[y]
        ans.append(xy)

    print(*ans, sep="\n")


def __starting_point():
    main()


__starting_point()
