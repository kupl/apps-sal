h, w = map(int, input().split())
C = [list(input()) for i in range(h)]
startls = []

for i in range(h):
    for j in range(w):
        if C[i][j] == '.':
            startls.append([i, j])

dy_dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for start in startls:
    visited = [[-1 for i in range(w)] for i in range(h)]
    visited[start[0]][start[1]] = 0
    cost = 0
    queue = [start]
    while len(queue) > 0:
        now = queue.pop(0)
        cost = visited[now[0]][now[1]] + 1
        for i in range(4):
            y = now[0] + dy_dx[i][0]
            x = now[1] + dy_dx[i][1]
            if 0 <= y < h and 0 <= x < w:
                if C[y][x] != '#' and visited[y][x] == -1:
                    visited[y][x] = cost
                    queue.append([y, x])
                    ans = max(ans, cost)
print(ans)
