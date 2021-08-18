from collections import deque
h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    cost = [[-1 for _ in range(w)] for _ in range(h)]
    que = deque()
    cost[i][j] = 0
    que.append((i, j))
    if s[i][j] == '
    return 0
    while que:
        ni, nj = que.popleft()
        for k in range(4):
            if 0 <= ni + dy[k] < h and 0 <= nj + dx[k] < w:
                if cost[ni + dy[k]][nj + dx[k]] != -1:
                    continue
                if s[ni + dy[k]][nj + dx[k]] == '.':
                    cost[ni + dy[k]][nj + dx[k]] = cost[ni][nj] + 1
                    que.append((ni + dy[k], nj + dx[k]))

    cc = 0
    for i in range(h):
        for j in range(w):
            if cost[i][j] > cc:
                cc = cost[i][j]
    return cc


ans = 0
for i in range(h):
    for j in range(w):
        cost = bfs(i, j)
        ans = max(ans, cost)

print(ans)
