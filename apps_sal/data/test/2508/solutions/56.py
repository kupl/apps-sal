from collections import deque
import sys


def bfs(xs, ys, d):
    queue = deque()
    queue.append((xs, ys, d))
    M[xs][ys] = d
    while queue:
        # queueには訪れた地点が入っている。そこから、4方向に移動できるか考え、queueから消す。
        x1, y1, d = queue.popleft()  # queueに入っていたものを消す。
        if [x1, y1] == [xg, yg]:  # もしゴールについていたならば、そのときの手数を出す。
            return

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            for k in range(1, K + 1):
                x2 = x1 + dx * k
                y2 = y1 + dy * k

                if (0 <= x2 < H) and (0 <= y2 < W):
                    if m[x2][y2] == "@":
                        break
                    elif M[x2][y2] == -1:  # まだ来たことない点だったという条件
                        M[x2][y2] = d + 1
                        queue.append((x2, y2, d + 1))  # 新しい点を足す。
                    elif M[x2][y2] < d + 1:
                        break
                else:
                    break


H, W, K = list(map(int, input().split()))
# K = min(K, max(H, W))
xs, ys, xg, yg = list(map(int, input().split()))
xs, ys, xg, yg = xs - 1, ys - 1, xg - 1, yg - 1

m = []
for i in range(H):
    m.append(list(map(str, sys.stdin.readline().strip())))

M = [[-1] * W for i in range(H)]

bfs(xs, ys, 0)

print((M[xg][yg]))
