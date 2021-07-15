def func(x):
    pass

def __starting_point():
    x = int(input())
    grid = {}
    for _ in range(x):
        row = input()
        if row not in grid:
            grid[row] = 1
        else:
            grid[row] += 1
    best_value = 0
    for key, value in list(grid.items()):
        if value > best_value:
            best_value = value
    print(best_value)

__starting_point()
