from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
(H, W) = map(int, input().split())
maze = []
for _ in range(H):
    maze.append(input())
(si, sj) = (0, 0)
(gi, gj) = (H - 1, W - 1)
didj = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(H, W, blocker='X'):
    while que != deque():
        (i, j) = que.popleft()
        for (di, dj) in didj:
            ni = i + di
            nj = j + dj
            if 0 <= ni and ni < H and (0 <= nj) and (nj < W) and (maze[ni][nj] != blocker) and (d[ni][nj] == INF):
                d[ni][nj] = d[i][j] + 1
                que.append((ni, nj))
    return


INF = H * W * 10
d = [[INF for x in range(W)] for x in range(H)]
d[si][sj] = 0
que = deque()
que.append((si, sj))
bfs(H, W, blocker='#')
if d[gi][gj] == INF:
    print(-1)
else:
    blc = 0
    for h in maze:
        for l in h:
            if l == '#':
                blc += 1
    score = H * W - blc - d[gi][gj] - 1
    print(score)
