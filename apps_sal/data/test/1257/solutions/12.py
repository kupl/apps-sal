def main():
    (n, k) = [int(t) for t in input().split()]
    grid = [[-1] * n for _ in range(n)]
    current = n * n
    for row in range(n):
        for column in range(n - 1, k - 2, -1):
            grid[row][column] = current
            current -= 1
    for row in range(n):
        for column in range(k - 2, -1, -1):
            grid[row][column] = current
            current -= 1
    s = sum((grid[row][k - 1] for row in range(n)))
    print(s)
    for row in range(n):
        print(' '.join((str(grid[row][column]) for column in range(n))))


def __starting_point():
    main()


__starting_point()
