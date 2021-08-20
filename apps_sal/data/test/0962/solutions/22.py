import sys
from collections import deque


def solve():
    (N, M) = map(int, input().split())
    edges = [set() for _ in range(N + 1)]
    for (a, b) in (map(int, line.split()) for line in sys.stdin):
        edges[a].add(b)
    for start in range(1, N + 1):
        visited = [0] * (N + 1)
        dq = deque([(start, {start})])
        visited[start] = 1
        while dq:
            (v, route) = dq.popleft()
            s = route & edges[v]
            if not (not s or s == {start}):
                continue
            for dest in edges[v]:
                if dest == start:
                    print(len(route))
                    print(*route, sep='\n')
                    return
                if visited[dest]:
                    continue
                visited[dest] = 1
                dq.append((dest, route | {dest}))
    print(-1)


def __starting_point():
    solve()


__starting_point()
