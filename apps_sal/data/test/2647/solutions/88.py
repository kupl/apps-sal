from collections import deque

h, w = list(map(int, input().split()))

s = [input() for _ in range(h)]

c = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            c += 1

# DFS
q = deque([[0, 0]])
dist = [[10000] * w for _ in range(h)]
dist[0][0] = 0

flag = False

while len(q) > 0:
    i, j = q.popleft()
    if i == h - 1 and j == w - 1:
        break
    else:
        if i < h - 1 and s[i + 1][j] == "." and not dist[i + 1][j] < 10000:
            q.append([i + 1, j])
            dist[i + 1][j] = dist[i][j] + 1
        if j < w - 1 and s[i][j + 1] == "." and not dist[i][j + 1] < 10000:
            q.append([i, j + 1])
            dist[i][j + 1] = dist[i][j] + 1
        if i > 0 and s[i - 1][j] == "." and not dist[i - 1][j] < 10000:
            q.append([i - 1, j])
            dist[i - 1][j] = dist[i][j] + 1
        if j > 0 and s[i][j - 1] == "." and not dist[i][j - 1] < 10000:
            q.append([i, j - 1])
            dist[i][j - 1] = dist[i][j] + 1

if dist[h - 1][w - 1] < 10000:
    print(h * w - dist[h - 1][w - 1] - 1 - c)
else:
    print(-1)
