from collections import deque

LOAD = "."

H, W = map(int, input().split())
field = [["" for _ in range(W)] for _ in range(H)]
dist = [[-1 for _ in range(W)] for _ in range(H)]
for h in range(H):
    field[h] = list(input())

total_laod = 0
for f in field:
    total_laod += f.count(LOAD)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sh, sw = (0, 0)
gh, gw = (H - 1, W - 1)
dist[sh][sw] = 0
q = deque()
q.append((sh, sw))

while q:
    h, w = q.popleft()
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]

        if nh < 0 or H <= nh or nw < 0 or W <= nw:
            continue
        if field[nh][nw] != LOAD:
            continue
        if dist[nh][nw] != -1:
            continue

        dist[nh][nw] = dist[h][w] + 1
        q.append((nh, nw))

if dist[gh][gw] == -1:
    print(-1)
else:
    print(total_laod - (dist[gh][gw] + 1))
