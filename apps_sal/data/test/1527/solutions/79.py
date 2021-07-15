from collections import deque

h, w = list(map(int, input().split()))
grid = [input() for _ in range(h)]

ans = 0

for startx in range(w):
    for starty in range(h):
        if grid[starty][startx] == "#":
            continue

        dist = [[10000]*w for _ in range(h)]
        dist[starty][startx] = 0
        maxDist = 0

        q = deque([(startx, starty)])

        while q:
            curx, cury = q.popleft()

            adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for xo, yo in adj:
                x, y = curx + xo, cury + yo

                if x < 0 or x >= w or y < 0 or y >= h:
                    continue
                if grid[y][x] == "#":
                    continue

                newDist = dist[cury][curx] + 1
                if newDist < dist[y][x]:
                    dist[y][x] = newDist
                    q.append((x, y))

                    maxDist = max(maxDist, newDist)

        ans = max(ans, maxDist)

print(ans)
