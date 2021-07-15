import sys
sys.setrecursionlimit(10 ** 7)

from collections import deque
INF = float('inf')
def resolve():
    H, W, K = list(map(int, input().split()))
    sx, sy, gx, gy = [int(x)-1 for x in input().split()]
    G = [list(input()) for _ in range(H)]

    dist = [[INF] * W for i in range(H)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])

    drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        x, y = q.popleft()
        if (x, y) == (gx, gy):
            print((dist[x][y]))
            return
        for dx, dy in drc:
            nx = x
            ny = y
            for k in range(K):
                nx += dx
                ny += dy
                if 0 <= nx < H and 0 <= ny < W and G[nx][ny] != '@':
                    if dist[nx][ny] <= dist[x][y]:
                        break
                    if dist[nx][ny] == INF:
                        q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                else:
                    break
    print((-1))

def __starting_point():
    resolve()

__starting_point()
