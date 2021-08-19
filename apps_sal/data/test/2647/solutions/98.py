from collections import deque
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
H, W = map(int, input().split())
M = ['#' * (W + 2)]
black = 0
for _ in range(H):
    row = input()
    M.append('#' + row + '#')
    black += row.count('#')
M.append('#' * (W + 2))
sy, sx = 1, 1
gy, gx = H, W
D = [[-1] * (W + 2) for _ in range(H + 2)]
D[sy][sx] = 0
visited = set()
q = deque()
q.append((sy, sx))
visited.add((sy, sx))
while q:
    y, x = q.popleft()
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if M[ny][nx] == '#' or D[ny][nx] != -1:
            continue
        D[ny][nx] = D[y][x] + 1
        q.append((ny, nx))
print(W * H - (D[gy][gx] + 1) - black if D[gy][gx] != -1 else -1)
