import collections

H, W = [int(n) for n in input().split()]
MAZE = []
for i in range(H):
    MAZE.append(list(input()))

def bfs(start_x, start_y):
    d = [[-1] * W for i in range(H)]

    dx_dy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    que = collections.deque([])
    que.append((start_x, start_y))

    d[start_x][start_y] = 0
    cnt = 0
    while(que):
        p = que.popleft()
        for dx, dy in dx_dy:
            nx = p[0] + dx
            ny = p[1] + dy

            if 0 <= nx < H and 0 <= ny < W and MAZE[nx][ny] != '#' and d[nx][ny] == -1:
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
            
                cnt = max(cnt, d[p[0]][p[1]] + 1)
        
    return cnt

max_count = 0
for i in range(H):
    for j in range(W):
        if MAZE[i][j] == '#':
            continue
        count = bfs(i, j)
        max_count = max(count, max_count)

print(max_count)
