from collections import deque
h, w = map(int, input().split())
maze = [['#'] * (w + 2) for i in range(h + 2)]
wall = 0
for i in range(1, h + 1):
    s = input()
    for j in range(1, w + 1):
        if s[j - 1] == '#':
            wall += 1
        maze[i][j] = s[j - 1]
queue = deque([[1, 1]])
maze[1][1] = 0
while queue:
    x, y = queue.popleft()
    if [x, y] != [h, w]:
        for n, m in ([0, -1], [0, 1], [-1, 0], [1, 0]):
            new_h, new_w = x + n, y + m
            if maze[new_h][new_w] == '.':
                maze[new_h][new_w] = maze[x][y] + 1
                queue.append([new_h, new_w])
            elif maze[new_h][new_w] != "#":
                maze[new_h][new_w] = min(maze[new_h][new_w], maze[x][y] + 1)
            else:
                pass
if maze[h][w] == '.' or maze[h][w] == '#':
    print(-1)
else:
    print(h * w - (maze[h][w] + 1) - wall)
