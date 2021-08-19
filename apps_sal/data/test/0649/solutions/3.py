from collections import defaultdict

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

#visited =[[[[False for _ in range(32)] for _ in range(8)] for _ in range(320)] for _ in range(320)]
visited = defaultdict(lambda: False)

grid = [[False for _ in range(320)] for _ in range(320)]


def dfs(x, y, d, n, N, inp):
    if n >= N or visited[(x, y, d, n)]:
        return

    visited[(x, y, d, n)] = True

    dist = inp[n]

    for i in range(1, dist + 1):
        grid[x + dx[d] * i][y + i * dy[d]] = True

    if (n < N):
        dfs(x + dx[d] * dist, y + dy[d] * dist, (d + 1) % 8, n + 1, N, inp)
        dfs(x + dx[d] * dist, y + dy[d] * dist, (d + 7) % 8, n + 1, N, inp)


def __starting_point():
    N = int(input())
    inp = list(map(int, input().strip().split()))
    dfs(160, 160, 0, 0, N, inp)
    result = sum(map(sum, grid))
    print(result)


__starting_point()
