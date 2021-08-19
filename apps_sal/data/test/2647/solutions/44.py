from collections import deque

H, W = map(int, input().split())

M = []

white = 0
for _ in range(H):
    M.append(input())
    white += M[-1].count('.')

q = deque()
q.append((0, 0))
visit = [0] * (H * W)
visit[0] = 1


def bfs():
    while q:
        x, y = q.popleft()
        for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x2 = x + dx
            y2 = y + dy

            if x2 < 0 or x2 > W - 1:
                continue
            if y2 < 0 or y2 > H - 1:
                continue

            if visit[y2 * W + x2]:
                continue
            if M[y2][x2] == '#':
                continue

            visit[y2 * W + x2] = visit[y * W + x] + 1

            if y2 == H - 1 and x2 == W - 1:
                return visit[y2 * W + x2]

            q.append((x2, y2))


steps = bfs()
ans = -1
if steps:
    ans = white - steps

print(ans)
