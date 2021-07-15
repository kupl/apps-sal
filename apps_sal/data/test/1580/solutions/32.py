# E - 1 or 2
from typing import List


def main():
    def dfs(source: int) -> None:
        stack = [source]
        is_visited[source] = True
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if is_visited[v]:
                    continue
                is_visited[v] = True
                stack.append(v)

    N, M, *X = list(map(int, open(0).read().split()))
    graph: List[List[int]] = [[] for _ in range(N + 1)]
    for x, y, _ in zip(*[iter(X)] * 3):
        graph[x].append(y), graph[y].append(x)

    is_visited = [False] * (N + 1)
    res = 0
    for i in range(1, N + 1):
        if is_visited[i]:
            continue
        res += 1
        dfs(i)
    print(res)


def __starting_point():
    main()

__starting_point()
