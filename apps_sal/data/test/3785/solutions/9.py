from queue import Queue, PriorityQueue
n, m, k = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(list(input()))
lvl = [[0] * m for i in range(n)]
x = y = -1
for i in range(n):
    if '.' in a[i]:
        x = i
        y = a[i].index('.')
        break
q = Queue()
q.put((x, y))
ans = []
lvl[x][y] = 1
while not q.empty():
    x, y = q.get()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if lvl[nx][ny]:
            continue
        if a[nx][ny] == '#':
            continue
        lvl[nx][ny] = lvl[x][y] + 1
        q.put((nx, ny))
        ans.append((-lvl[nx][ny], nx, ny))
ans.sort()
for i in range(k):
    _, x, y = ans[i]
    a[x][y] = 'X'
print('\n'.join(''.join(l) for l in a))
