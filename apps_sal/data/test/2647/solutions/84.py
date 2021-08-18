from collections import deque
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
H, W = map(int, input().split())
M = []
visited = [[0] * W for _ in range(H)]
D = [[0] * W for _ in range(H)]
black = 0
for _ in range(H):
    s = input()
    M.append(s)
    for c in s:
        if c == '
        black += 1
q = deque()
q.append((0, 0))
cost = -1
while q:
    y, x = q.popleft()
    d = D[y][x]
    if x == W - 1 and y == H - 1:
        cost = d
        break
    if visited[y][x] == 1:
        continue
    else:
        visited[y][x] = 1
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if (0 <= nx < W) and (0 <= ny < H):
                if visited[ny][nx] == 0 and M[ny][nx] == '.':
                    D[ny][nx] = d + 1
                    q.append((ny, nx))
if cost == -1:
    print(-1)
else:
    print(H * W - cost - 1 - black)
