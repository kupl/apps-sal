import sys
from queue import deque

# sys.stdin = open('ivo.in')

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m, k = map(int, sys.stdin.readline().split())

a = []
for i in range(n):
    a.append(sys.stdin.readline().rstrip())


visited = []
values = []
for x in range(n):
    visited.append([])
    values.append([])
    for y in range(m):
        visited[x].append(False)
        values[x].append(0)


for x in range(n):
    for y in range(m):
        if a[x][y] == '*' or visited[x][y]:
            continue
        q = deque()
        visited[x][y] = True
        q.append((x, y))
        sum = 0
        connected = [(x, y)]
        while len(q) != 0:
            cur = q.pop()
            for l in move:
                tx = cur[0] + l[0]
                ty = cur[1] + l[1]
                if tx < 0 or tx >= n or ty < 0 or ty >= m:
                    continue
                if a[tx][ty] == '.' and visited[tx][ty]:
                    continue
                if a[tx][ty] == '*':
                    sum += 1
                    continue
                q.append((tx, ty))
                visited[tx][ty] = True
                connected.append((tx, ty))
        for c in connected:
            values[c[0]][c[1]] = sum

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    print(values[x - 1][y - 1])
