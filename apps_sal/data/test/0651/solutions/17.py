import itertools

n, m = list(map(int, input().split()))
maze = [input() for i in range(n)]
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            sy = i
            sx = j
        elif maze[i][j] == 'E':
            ey = i
            ex = j
s = [int(c) for c in input()]
cnt = 0
for p in itertools.permutations([(0, 1), (0, -1), (1, 0), (-1, 0)], r=4):
    y = sy
    x = sx
    for i in s:
        dy, dx = p[i]
        if 0 <= y + dy < n and 0 <= x + dx < m and maze[y + dy][x + dx] != '#':
            y += dy
            x += dx
        else:
            break
        if y == ey and x == ex:
            break
    if y == ey and x == ex:

        cnt += 1
print(cnt)
