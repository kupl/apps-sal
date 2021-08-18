
NO_SOL = -1


def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    zero = None
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
        if zero is None:
            try:
                zero = (i, grid[i].index(0))
            except Exception:
                zero = None
    sum_sample = None
    for i in range(n):
        if i == zero[0]:
            continue
        else:
            sum_sample = sum(grid[i])
            break
    zero_cand = sum_sample - sum(grid[zero[0]])
    if zero_cand <= 0:
        print(NO_SOL)
        return
    grid[zero[0]][zero[1]] = zero_cand
    for row in grid:
        if sum(row) != sum_sample:
            print(NO_SOL)
            return
    for column in zip(*grid):
        if sum(column) != sum_sample:
            print(NO_SOL)
            return
    if sum(grid[i][i] for i in range(n)) != sum_sample:
        print(NO_SOL)
        return
    if sum(grid[i][n - i - 1] for i in range(n)) != sum_sample:
        print(NO_SOL)
        return
    print(zero_cand)


def __starting_point():
    main()


__starting_point()
