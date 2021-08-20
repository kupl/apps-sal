from collections import deque
(H, W) = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
d = deque([])
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        d.append((i, j, 0))
        visited = [[-1] * W for _ in range(H)]
        visited[i][j] = 0
        while d:
            (x, y, c) = d.popleft()
            for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                (nx, ny) = (x + dx, y + dy)
                if 0 <= nx < H and 0 <= ny < W and (visited[nx][ny] == -1) and (S[nx][ny] == '.'):
                    visited[nx][ny] = c + 1
                    d.append((nx, ny, c + 1))
        ans = max(ans, c)
print(ans)
