import itertools


def main():
    grid = [list(map(int, input().split())) for i in range(3)]
    all = sum(sum(grid, []))
    a = [0] * 3
    b = [0] * 3
    for i, j, k in itertools.product(list(range(grid[0][0] + 1)), list(range(grid[1][1] + 1)), list(range(grid[2][2] + 1))):
        a = [i, j, k]
        b = [grid[idx][idx] - v for idx, v in enumerate(a)]
        if (sum(a) * 3) + (sum(b) * 3) == all:
            print("Yes")
            return
    print('No')


def __starting_point():
    main()


__starting_point()
