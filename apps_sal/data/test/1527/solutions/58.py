import collections

H, W = map(int, input().split())
maze = [[None for _ in range(W)] for _ in range(H)]

for i in range(H):
    maze[i] = list(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0

for j in range(H):
    for k in range(W):
        if maze[j][k] == '
            continue
        else:
            sy = j
            sx = k

            seen = [[-1 for _ in range(W)] for _ in range(H)]
            seen[sy][sx] = 0

            que = collections.deque()
            que.append([sy, sx])

            while(len(que) != 0):
                p = que.popleft()
                for i in range(4):
                    ny = p[0] + dy[i]
                    nx = p[1] + dx[i]
                    if (ny >= 0 and nx >= 0 and ny < H and nx < W and seen[ny][nx] == -1 and maze[ny][nx] != '
                        seen[ny][nx]=seen[p[0]][p[1]] + 1
                        que.append([ny, nx])

            cnt=max(cnt, max([x for row in seen for x in row]))

print(cnt)
