from collections import deque


def bfs(start):
    q = deque([[start]])
    visited = set()
    while q:
        path = q.popleft()
        i, j = path[-1]
        if (i, j) == (H - 1, W - 1):
            return path
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < H and
                0 <= nj < W and
                field[ni][nj] != "#" and
                (ni, nj) not in visited
            ):
                q.append(path + [(ni, nj)])
                visited.add((ni, nj))


H, W = list(map(int, input().split()))
field = [input() for _ in range(H)]
shortest_path = bfs((0, 0))
if shortest_path is None:
    print((-1))
    return
ans = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == "." and (i, j) not in shortest_path:
            ans += 1
print(ans)
