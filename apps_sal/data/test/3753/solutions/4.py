import sys

readLn = sys.stdin.readline


def __starting_point():
    n, m = list(map(int, readLn().split()))
    ds = [[-1 if c == '#' else 0 for c in readLn()] for _ in range(n)]
    ds[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            if ds[i][j] == 0:
                if i > 0 and ds[i - 1][j] > 0:
                    ds[i][j] = ds[i - 1][j] + 1
                if j > 0 and ds[i][j - 1] > 0:
                    ds[i][j] = ds[i][j - 1] + 1
    if ds[n - 1][m - 1] == 0:
        print(0)
    else:
        ds[n - 1][m - 1] = -2
        sm = [0 for _ in range(n + m + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if ds[i][j] > 1 and ((i + 1 < n and ds[i + 1][j] == -2) or (j + 1 < m and ds[i][j + 1] == -2)):
                    sm[ds[i][j]] += 1
                    ds[i][j] = -2
        ans = 2
        for i in range(2, n + m):
            if sm[i] == 1:
                ans = 1
                break
        print(ans)


__starting_point()
