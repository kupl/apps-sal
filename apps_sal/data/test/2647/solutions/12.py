from queue import Queue
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

H, W = list(map(int, input().split()))
S = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
que = Queue()

# 初期条件
dist[0][0] = 0
que.put((0, 0))

# 幅優先探索
while not que.empty():
    x, y = que.get()
    for dir in range(4):
        x2, y2 = x + dx[dir], y + dy[dir]
        if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W or S[x2][y2] == '#':
            continue
        if dist[x2][y2] != -1:
            continue
        dist[x2][y2] = dist[x][y] + 1
        que.put((x2, y2))

# 白マス数
white = sum(sum(1 if S[x][y] == '.' else 0 for y in range(W)) for x in range(H))

# 答え
print((white - dist[H - 1][W - 1] - 1 if dist[H - 1][W - 1] != -1 else -1))
