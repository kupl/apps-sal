from collections import deque


def bfs(start, goal):
    q = deque([[start]])
    visited = set()
    while q:
        path = q.popleft()
        i, j = path[-1]
        if (i, j) == goal:
            return path
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < H and 0 <= nj < W and field[ni][nj] == "."):
                continue
            if (ni, nj) not in visited:
                q.append(path + [(ni, nj)])
                visited.add((ni, nj))
    return []


H, W = list(map(int, input().split()))
field = [input() for _ in range(H)]
shortest_path = bfs((0, 0), (H - 1, W - 1))
if shortest_path:
    print((sum(v == "." for row in field for v in row) - len(shortest_path)))
else:
    print((-1))
