from collections import deque
import sys


def bfs(xs, ys):
    queue = deque([[xs, ys]])
    M[xs][ys] = 0
    while queue:
        # queueには訪れた地点が入っている。そこから、4方向に移動できるか考え、queueから消す。
        x1, y1 = queue.popleft()  # queueに入っていたものを消す。
        if [x1, y1] == [xg, yg]:  # もしゴールについていたならば、そのときの手数を出す。
            return M[x1][y1]

        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            for k in range(1, K + 1):
                new_x = x1 + dx * k
                new_y = y1 + dy * k

                if (0 <= new_x < H) and (0 <= new_y < W):
                    if m[new_x][new_y] == "@":
                        break
                    elif M[new_x][new_y] == -1:  # まだ来たことない点だったという条件
                        M[new_x][new_y] = M[x1][y1] + 1
                        queue.append([new_x, new_y])  # 新しい点を足す。
                    elif M[new_x][new_y] < M[x1][y1] + 1:
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

bfs(xs, ys)

print((M[xg][yg]))
