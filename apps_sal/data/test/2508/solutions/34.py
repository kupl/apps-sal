import sys
from collections import deque


def bfs(x1, y1, d):
    q = deque([])
    q.append((d, x1, y1))

    while q:
        d, x1, y1 = q.popleft()
        M[x1][y1] = d

        if [x1, y1] == [xg, yg]:
            print(d)
            return

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            for k in range(1, K + 1):
                x2 = x1 + dx * k
                y2 = y1 + dy * k
                if x2 < 0 or x2 >= H:
                    break
                if y2 < 0 or y2 >= W:
                    break
                if m[x2][y2] == '@':
                    break
                if M[x2][y2] < d + 1:
                    break
                if M[x2][y2] == d + 1:
                    continue

                q.append((d + 1, x2, y2))
                M[x2][y2] = d + 1

    print((-1))


H, W, K = list(map(int, sys.stdin.readline().strip().split()))
xs, ys, xg, yg = list(map(int, sys.stdin.readline().strip().split()))
xg -= 1
yg -= 1

m = []
for _ in range(H):
    m.append(list(map(str, sys.stdin.readline().strip())))

M = [[float('inf')] * W for _ in range(H)]

bfs(xs - 1, ys - 1, 0)
