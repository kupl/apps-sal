from collections import deque
H, W = map(int, input().split())
S = [list(input())for _ in range(H)]


def bfs(h, w, sy, sx, gy, gx, S):
    maze = [[10**9] * (W)for _ in range(H)]
    maze[sy - 1][sx - 1] = 0
    que = deque([[sy - 1, sx - 1]])
    while que:
        y, x = que.popleft()
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nexty, nextx = y + i, x + j
            if 0 <= nexty < h and 0 <= nextx < w:
                dist1 = S[nexty][nextx]
                dist2 = maze[nexty][nextx]
            else:
                continue
            if dist1 != '#':
                if dist2 > maze[y][x] + 1:
                    maze[nexty][nextx] = maze[y][x] + 1
                    que.append([nexty, nextx])
    return maze[gy - 1][gx - 1] + 1


A = 0
for s in S:
    A += s.count('.')

B = bfs(H, W, 1, 1, H, W, S)
if B > 10**9:
    ans = -1
else:
    ans = A - B
print(ans)
