import copy
H, W = map(int, input().split())

maze = []
maze.append(['#'] * (W + 2))
for i in range(H):
    line = input()
    line_n = ['#'] + [line[i] for i in range(W)] + ['#']
    maze.append(line_n)
maze.append(['#'] * (W + 2))
for i in range(H + 2):
    for j in range(W + 2):
        if maze[i][j] == '#':
            maze[i][j] = 9
maze_copy = copy.deepcopy(maze)
global_max = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        maze = copy.deepcopy(maze_copy)
        sx = i
        sy = j
        if maze[i][j] != 9:
            pos = [[sx, sy, 0]]
            max_depth = 0
            while len(pos) > 0:
                x, y, depth = pos.pop(0)
                # print(x,y)
                if depth > max_depth:
                    max_depth = depth
                # 探索終了条件
                maze[x][y] = 0
                if maze[x - 1][y] == '.':
                    pos.append([x - 1, y, depth + 1])
                    maze[x - 1][y] = 0
                if maze[x][y - 1] == '.':
                    pos.append([x, y - 1, depth + 1])
                    maze[x][y - 1] = 0
                if maze[x + 1][y] == '.':
                    pos.append([x + 1, y, depth + 1])
                    maze[x + 1][y] = 0
                if maze[x][y + 1] == '.':
                    pos.append([x, y + 1, depth + 1])
                    maze[x][y + 1] = 0
            # print("max_depth={}".format(max_depth))
            if max_depth > global_max:
                global_max = max_depth
print(global_max)
