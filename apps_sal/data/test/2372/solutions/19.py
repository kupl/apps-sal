from collections import deque


def bfs():
    (H, W) = map(int, input().split())
    (sy, sx) = map(int, input().split())
    (gy, gx) = map(int, input().split())
    S = ['#' * (W + 4), '#' * (W + 4)]
    for _ in range(H):
        S.append('##' + input() + '##')
    S.append('#' * (W + 4))
    S.append('#' * (W + 4))
    dist = [[-2] * (W + 4) for _ in range(H + 4)]
    for i in range(H + 4):
        for j in range(W + 4):
            if S[i][j] == '.':
                dist[i][j] = -1
    dist[sy + 1][sx + 1] = 0
    A = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    B = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) > 1]
    que = deque([[sx + 1, sy + 1]])
    que2 = deque([])
    while que:
        (x, y) = que.popleft()
        que2.appendleft([x, y])
        for (dx, dy) in A:
            nx = x + dx
            ny = y + dy
            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x]
                que.appendleft([nx, ny])
        if que:
            continue
        while que2:
            (x, y) = que2.popleft()
            for (dx, dy) in B:
                nx = x + dx
                ny = y + dy
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    que.append([nx, ny])
    ans = dist[gy + 1][gx + 1]
    return ans


print(bfs())
