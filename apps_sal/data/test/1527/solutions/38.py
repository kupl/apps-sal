from collections import deque
h, w = list(map(int, input().split()))

s = []
s.append(list("#" * (w + 2)))
start = []
for i in range(1, h + 1):
    wk = list("#" + input() + "#")
    for j in range(1, w + 1):
        if wk[j] == ".":
            start.append([i, j])
    s.append(wk)
s.append(list("#" * (w + 2)))

dist = [[-1] * (w + 2) for _ in range(h + 2)]


def bfs(start):
    que = deque([start])
    dist[start[0]][start[1]] = 0
    end = []
    cnt = 0
    while que:
        y, x = que.popleft()
        for py, px in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + py, x + px
            if s[ny][nx] == "." and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                que.append([ny, nx])
                cnt = max(cnt, dist[y][x] + 1)
    return cnt


ans = 0
for i in start:
    ans = max(ans, bfs(i))
    dist = [[-1] * (w + 2) for _ in range(h + 2)]
print(ans)
