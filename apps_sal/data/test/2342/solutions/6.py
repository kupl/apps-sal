import sys
input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    (h, w) = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    good = set()
    bad = set()
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'G':
                good.add((i, j))
            elif grid[i][j] == 'B':
                bad.add((i, j))
    if not good:
        ans.append('Yes')
        continue
    flg = 0
    for (ci, cj) in bad:
        for (di, dj) in delta:
            (ni, nj) = (ci + di, cj + dj)
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] == '.':
                    grid[ni][nj] = '#'
                elif grid[ni][nj] == 'G':
                    flg = 1
                    break
        if flg:
            break
    if flg or grid[h - 1][w - 1] == '#':
        ans.append('No')
        continue
    q = [(h - 1, w - 1)]
    vis = [[0] * w for _ in range(h)]
    vis[-1][-1] = 1
    while q:
        (ci, cj) = q.pop()
        for (di, dj) in delta:
            (ni, nj) = (ci + di, cj + dj)
            if 0 <= ni < h and 0 <= nj < w and (grid[ni][nj] != '#') and (not vis[ni][nj]):
                vis[ni][nj] = 1
                q.append((ni, nj))
    if all((vis[i][j] for (i, j) in good)):
        ans.append('Yes')
    else:
        ans.append('No')
print('\n'.join(ans))
