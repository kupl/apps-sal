from collections import deque
x0, y0, x1, y1 = map(int, input().split())
n = int(input())
g = {}
for _ in range(n):
    r, a, b = map(int, input().split())
    for i in range(a, b + 1):
        g[(r, i)] = -1
g[(x0, y0)] = 0
q = deque([(x0, y0)])
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
while len(q) > 0:
    c = q.popleft()
    for i in range(8):
        m = (c[0] + dx[i], c[1] + dy[i])
        if m in g and g[m] == -1:
            q.append(m)
            g[m] = g[c] + 1

print(g[(x1, y1)])
return
