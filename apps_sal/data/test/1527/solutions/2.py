import queue
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = 0
for sx in range(H):
    for sy in range(W):
        if S[sx][sy] == '
        continue

        D = [[float('inf') for _ in range(W)] for _ in range(H)]
        D[sx][sy] = 0
        q = queue.Queue()
        q.put((sx, sy))

        vs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while not q.empty():
            x, y = q.get()
            for dx, dy in vs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < H and 0 <= ny < W and S[nx][ny] != '
                q.put((nx, ny))
                D[nx][ny] = D[x][y] + 1

        for gx in range(H):
            for gy in range(W):
                if S[gx][gy] == '
                continue
                ans = max(ans, D[gx][gy])

print(ans)
