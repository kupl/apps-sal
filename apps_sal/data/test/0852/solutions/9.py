import sys


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


INF = 10 ** 19
MOD = 10 ** 9 + 7


def bfs(grid, src):
    from collections import deque
    (H, W) = (len(grid), len(grid[0]))
    visited = list3d(2, H, W, 0)
    que = deque()
    for (h, w) in src:
        que.append((0, h, w))
        que.append((1, h, w))
        visited[0][h][w] = 1
        visited[1][h][w] = 1
    while que:
        (up, h, w) = que.popleft()
        if w == N - 1:
            return True
        if h == 0:
            up = 1
        if h == K:
            up = 0
        if up:
            if not visited[up][h + 1][w] and grid[h + 1][w] <= L:
                visited[up][h + 1][w] = 1
                que.append((up, h + 1, w))
            if not visited[up][h + 1][w + 1] and grid[h + 1][w + 1] <= L:
                visited[up][h + 1][w + 1] = 1
                que.append((up, h + 1, w + 1))
        else:
            if not visited[up][h - 1][w]:
                visited[up][h - 1][w] = 1
                que.append((up, h - 1, w))
            if not visited[up][h - 1][w + 1] and grid[h - 1][w + 1] <= L:
                visited[up][h - 1][w + 1] = 1
                que.append((up, h - 1, w + 1))
    return False


for _ in range(INT()):
    (N, K, L) = MAP()
    A = LIST()
    grid = list2d(K + 1, N, 0)
    for i in range(K + 1):
        for j in range(N):
            grid[i][j] = A[j] + i
    src = []
    for i in range(K + 1):
        if grid[i][0] <= L:
            src.append((i, 0))
    ok = False
    for x in range(K + 1):
        if bfs(grid, src):
            Yes()
            break
    else:
        No()
