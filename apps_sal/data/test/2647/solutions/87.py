import sys
H, W = map(int, input().split())
C = [list(input()) for i in range(H)]
cost = [[-1 for i in range(W)] for i in range(H)]
queue = []

black = 0
for i in range(H):
    black += C[i].count('#')

queue.append([0, 0])
cost[0][0] = 0

dy_dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while len(queue) > 0:
    now = queue.pop(0)
    if now[0] == H - 1 and now[1] == W - 1:
        ans = H * W - cost[H - 1][W - 1] - black - 1
        print(ans)
        return
    for i in range(4):
        y = now[0] + dy_dx[i][0]
        x = now[1] + dy_dx[i][1]
        if 0 <= y < H and 0 <= x < W:
            if C[y][x] != '#' and cost[y][x] == -1:
                cost[y][x] = cost[now[0]][now[1]] + 1
                queue.append([y, x])
print(-1)
