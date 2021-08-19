(H, W) = map(int, input().split())
s = [list(input()) for j in range(H)]


def bfs(h, w):
    checked = [[False for i in range(W)] for j in range(H)]
    q = [(h, w, 0)] if s[h][w] == '.' else []
    checked[h][w] = True
    g_n = 0
    while q:
        (h_, w_, n) = q.pop(0)
        g_n = max(n, g_n)
        for (i, j) in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            if 0 <= h_ + i < H and 0 <= w_ + j < W:
                if checked[h_ + i][w_ + j]:
                    continue
                checked[h_ + i][w_ + j] = True
                if s[h_ + i][w_ + j] == '.':
                    q.append((h_ + i, w_ + j, n + 1))
    return g_n


n = 0
for i in range(H):
    for j in range(W):
        n = max(n, bfs(i, j))
print(n)
