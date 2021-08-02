from collections import deque


def bfs(start, goal, g, n, visited):
    visited1 = [False] * (n + 1)
    visited2 = [False] * (n + 1)
    q = deque([start])
    visited[start] = 0
    while q:
        curr_node = q.popleft()
        if curr_node == goal:
            return
        for next1_node in g[curr_node]:
            if visited1[next1_node]:
                continue
            visited1[next1_node] = True
            for next2_node in g[next1_node]:
                if visited2[next2_node]:
                    continue
                visited2[next2_node] = True
                for next3_node in g[next2_node]:
                    if visited[next3_node] >= 0:
                        continue
                    visited[next3_node] = visited[curr_node] + 1
                    q.append(next3_node)


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)

    s, t = map(int, input().split())

    visited = [-1] * (n + 1)
    visited[0] = 0

    bfs(s, t, g, n, visited)
    print(visited[t])


def __starting_point():
    main()


__starting_point()
