def main():
    n = int(input())
    N = n + 1
    row1 = [int(c) for c in input().split()]
    row2 = [int(c) for c in input().split()]
    grid = [row1, row2]
    sum123 = [[0] * N, [0] * N]
    sum321 = [[0] * N, [0] * N]
    sum111 = [[0] * N, [0] * N]
    for i in range(2):
        for j in range(n - 1, -1, -1):
            sum123[i][j] = sum123[i][j + 1] + (j + 1) * grid[i][j]
            sum321[i][j] = sum321[i][j + 1] + (n - j) * grid[i][j]
            sum111[i][j] = sum111[i][j + 1] + grid[i][j]
    res = _sum = i = 0
    for j in range(n):
        nres = _sum
        nres += sum123[i][j] + j * sum111[i][j]
        nres += sum321[i ^ 1][j] + (j + n) * sum111[i ^ 1][j]
        res = max(res, nres)
        _sum += grid[i][j] * (j + j + 1)
        _sum += grid[i ^ 1][j] * (j + j + 2)
        i ^= 1
    for j in range(n):
        res -= grid[0][j] + grid[1][j]
    print(res)


def __starting_point():
    main()


__starting_point()
