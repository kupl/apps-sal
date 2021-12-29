from collections import deque
(R, C) = map(int, input().split())
masu = [list(input()) for _ in range(R)]
(sr, sc) = (0, 0)
(gr, gc) = (R - 1, C - 1)


def bfs():
    d = [[float('inf')] * C for _ in range(R)]
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    que = deque([])
    que.append((sr, sc))
    d[sr][sc] = 0
    while que:
        p = que.popleft()
        if p[0] == gr and p[1] == gc:
            break
        for i in range(4):
            nr = p[0] + dr[i]
            nc = p[1] + dc[i]
            if 0 <= nr < R and 0 <= nc < C and (masu[nr][nc] != '#') and (d[nr][nc] == float('inf')):
                que.append((nr, nc))
                d[nr][nc] = d[p[0]][p[1]] + 1
    return d[gr][gc]


white = 0
for i in range(R):
    for j in range(C):
        if masu[i][j] == '.':
            white += 1
res = bfs()
if 0 < res < float('inf'):
    print(white - res - 1)
else:
    print(-1)
