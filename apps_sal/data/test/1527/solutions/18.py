h, w = map(int, input().split())
C = [list(input()) for i in range(h)]

queue = []
visited = []
visited = [[0 for i in range(w)] for i in range(h)]
ans = 0

for i in range(h):
    for j in range(w):
        if C[i][j] == '.':
            queue.append([i, j])
            visited[i][j] = 1

            dy_dx = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while len(queue) > 0:
                now = queue.pop(0)
                for k in range(4):
                    y = now[0] + dy_dx[k][0]
                    x = now[1] + dy_dx[k][1]
                    if 0 <= y < h and 0 <= x < w:
                        if C[y][x] != '
                        visited[y][x] = visited[now[0]][now[1]] + 1
                        queue.append([y, x])

        for l in range(h):
            for m in range(w):
                ans = max(ans, visited[l][m])

        queue = []
        visited = [[0 for i in range(w)] for i in range(h)]

print(ans - 1)
