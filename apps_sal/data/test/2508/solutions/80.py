from collections import deque

H, W, K = map(int, input().split())
x1, y1, x2, y2 = (int(i) - 1 for i in input().split())
C = [input() for _ in range(H)]

ans = [[-1] * W for _ in range(H)]
ans[x1][y1] = 0

Q = deque([(x1, y1)])
while Q:
    x, y = Q.popleft()
    if (x, y) == (x2, y2):
        print(ans[x][y])
        return

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for a in range(1, K + 1):
            nx = x + a * di
            ny = y + a * dj

            if not (0 <= nx < H and 0 <= ny < W) or C[nx][ny] == "@" or 0 <= ans[nx][ny] <= ans[x][y]:
                break

            if ans[nx][ny] == -1:
                Q.append((nx, ny))

            ans[nx][ny] = 1 + ans[x][y]

print(-1)
