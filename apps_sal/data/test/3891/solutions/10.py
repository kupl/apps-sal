USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    (n, m) = list(map(int, input().split(' ')))
    grid = []
    for _ in range(n):
        grid.append(input())
    (x0, y0) = (n, m)
    (x1, y1) = (0, 0)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                x0 = min(x0, i)
                y0 = min(y0, j)
                x1 = max(x1, i)
                y1 = max(y1, j)
    print((x0 + x1) // 2 + 1, (y0 + y1) // 2 + 1)


def __starting_point():
    main()


__starting_point()
