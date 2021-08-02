from collections import deque


MAX_H = 20
MAX_W = 20


H, W = [int(x) for x in input().split()]
S = [input() for _ in range(H)]


def valid(i, j, B):
    return 0 <= i < H and 0 <= j < W and S[i][j] == '.' and not B[i][j]


def bfs(i, j):
    B = [[False] * W for _ in range(H)]
    dist = 0
    q = deque([[i, j, -1]])
    while len(q) > 0:
        p = q.popleft()
        i = p[0]
        j = p[1]
        if B[i][j]:
            continue
        d = p[2] + 1
        dist = max(dist, d)
        B[i][j] = True
        if valid(i - 1, j, B):
            q.append([i - 1, j, d])
        if valid(i + 1, j, B):
            q.append([i + 1, j, d])
        if valid(i, j - 1, B):
            q.append([i, j - 1, d])
        if valid(i, j + 1, B):
            q.append([i, j + 1, d])
    return dist


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            ans = max(ans, bfs(i, j))
print(ans)
