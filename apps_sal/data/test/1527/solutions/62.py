
h, w = map(int, input().split())
s = [list(input())for i in range(h)]

visited = [[0 for i in range(w)] for j in range(h)]
quene = []
ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            quene.append([i, j])
            visited[i][j] = 1

            dy_dx = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while len(quene) >= 1:
                now = quene.pop(0)
                for k in range(4):
                    y = now[0] + dy_dx[k][0]
                    x = now[1] + dy_dx[k][1]
                    if 0 <= y < h and 0 <= x < w:
                        if s[y][x] != "
                        visited[y][x] = visited[now[0]][now[1]] + 1
                        quene.append([y, x])
        for l in range(h):
            for m in range(w):
                ans = max(ans, visited[l][m])
        visited = [[0 for i in range(w)] for j in range(h)]
print(ans - 1)
