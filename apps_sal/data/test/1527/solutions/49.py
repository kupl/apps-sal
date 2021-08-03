from collections import deque
import copy

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def bfs(x, y):
    check = copy.deepcopy(S)
    que = deque()
    que.append((x, y))
    check[y][x] = 0
    while que.__len__() != 0:
        x, y = que.popleft()
        tmp = check[y][x]
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            sx = x + dx
            sy = y + dy
            if -1 < sx < W and -1 < sy < H:
                if check[sy][sx] == '.':
                    check[sy][sx] = tmp + 1
                    que.append((sx, sy))
    return tmp


ans = 0
for x in range(W):
    for y in range(H):
        if S[y][x] == '.':
            ans = max(bfs(x, y), ans)

print(ans)
