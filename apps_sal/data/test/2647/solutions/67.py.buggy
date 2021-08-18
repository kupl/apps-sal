import sys
h, w = list(map(int, input().split()))
ss = [list(input()) for i in range(h)]
num = 0
for i in range(h):
    num += ss[i].count('.')

visited = [[0 for i in range(w)] for j in range(h)]
queue = []
queue.append([0, 0])
ss[0][0] = 'fin'
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


while len(queue) > 0:
    now = queue.pop(0)
    for i in range(4):
        x = now[1] + dx[i]
        y = now[0] + dy[i]
        if 0 <= x < w and 0 <= y < h:
            if ss[y][x] == '.' and visited[y][x] == 0:
                visited[y][x] = visited[now[0]][now[1]] + 1
                queue.append([y, x])
            if x == w - 1 and y == h - 1:
                print((num - visited[y][x] - 1))
                return
print((-1))
