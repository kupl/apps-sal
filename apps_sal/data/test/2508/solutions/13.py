import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def main():

    h, w, k = map(int, input().split())
    xs, ys, xg, yg = map(lambda x: int(x) - 1, input().split())
    field = [input() for _ in range(h)]

    inf = 1e7

    dist = [[inf] * w for _ in range(h)]
    dist[xs][ys] = 0
    que = deque([(xs, ys)])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x, y
            for _ in range(k):
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    break
                if field[nx][ny] == '@' or dist[nx][ny] <= dist[x][y]:
                    break
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx, ny))

    if dist[xg][yg] == inf:
        print(-1)
    else:
        print(dist[xg][yg])


def __starting_point():
    main()


__starting_point()
