(H, W) = list(map(int, input().split()))
maze = [input() for i in range(H)]
direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(sy, sx):
    reached = [[-1] * W for _ in range(H)]
    reached[sy][sx] = 0
    from collections import deque
    que = deque([[sy, sx]])
    while que:
        (iy, ix) = que.popleft()
        for d in direction:
            (tx, ty) = (ix + d[0], iy + d[1])
            if tx >= W or ty >= H or tx < 0 or (ty < 0):
                continue
            if reached[ty][tx] != -1 or maze[ty][tx] == '#':
                continue
            reached[ty][tx] = reached[iy][ix] + 1
            que.append([ty, tx])
    d_max = 0
    for i in range(H):
        for j in range(W):
            d_max = max(d_max, reached[i][j])
    return d_max


ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            ans = max(ans, bfs(i, j))
print(ans)
