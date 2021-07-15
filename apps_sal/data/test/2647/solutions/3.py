from collections import deque

h, w = list(map(int, input().split()))
grid = [input() for _ in range(h)]

q = deque([(0, 0)])
dists = [[10000] * w for _ in range(h)]
dists[0][0] = 0
prev = [[-1] * w for _ in range(h)]

while q:
    x, y = q.popleft()

    nei = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for xo, yo in nei:
        nextx, nexty = x+xo, y+yo

        if nextx < 0 or nextx >= w or nexty < 0 or nexty >= h:
            continue
        if grid[nexty][nextx] == "#":
            continue

        dist = dists[y][x]+1

        if dist < dists[nexty][nextx]:
            dists[nexty][nextx] = dist
            prev[nexty][nextx] = (x, y)
            q.append((nextx, nexty))

if prev[h-1][w-1] != -1:
    path = []
    cur = (w-1, h-1)

    while cur != -1:
        path.append(cur)
        cur = prev[cur[1]][cur[0]]

    cnt = 0
    for i in range(w):
        for j in range(h):
            if grid[j][i] == "." and (i, j) not in path:
                cnt += 1

    print(cnt)
else:
    print(-1)
