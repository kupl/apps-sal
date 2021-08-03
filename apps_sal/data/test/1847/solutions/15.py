from collections import deque

x0, y0, x1, y1 = list(map(int, input().split()))
n = int(input())
allowed = {}
for i in range(n):
    r, a, b = list(map(int, input().split()))
    for j in range(a, b + 1):
        allowed[(r, j)] = True


visited = {}
q = deque()
q.append((x0, y0))
visited[(x0, y0)] = 0
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
result = -1
while len(q) > 0:
    x, y = q.popleft()
    original_dist = visited[x, y]
    if x == x1 and y == y1:
        result = original_dist
        break
    for i in range(len(dir)):
        dx, dy = dir[i]
        nx, ny = x + dx, y + dy
        if (nx, ny) in allowed and (nx, ny) not in visited:
            q.append((nx, ny))
            visited[(nx, ny)] = original_dist + 1
print(result)
