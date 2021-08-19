from collections import deque

H, W = list(map(int, input().split()))
S = [[c == '#' for c in input()] for _ in range(H)]


def bfs(i, j):
    if S[i][j]:
        return 0
    que = deque()
    que.append((i, j))
    vis = [row[:] for row in S]
    vis[i][j] = 1
    ans = -1
    while que:
        ans += 1
        for _ in range(len(que)):
            i, j = que.popleft()
            for ni, nj in nbs(i, j):
                if not vis[ni][nj]:
                    que.append((ni, nj))
                    vis[ni][nj] = 1
    return ans


def nbs(i, j):
    for ni, nj in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1):
        if 0 <= ni < H and 0 <= nj < W:
            yield ni, nj


ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, bfs(i, j))

print(ans)
