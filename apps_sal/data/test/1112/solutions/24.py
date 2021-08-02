def main():
    def is_valid(grid):
        if sum(grid[0]) != sum(grid[1]) or sum(grid[1]) != sum(grid[2]):
            return False
        if grid[0][0] + grid[1][1] + grid[2][2] != grid[0][2] + grid[1][1] + grid[2][0]:
            return False
        return True

    grid = []
    for i in range(3):
        grid.append(list(map(int, input().split(' '))))

    s = sum(grid[0]) + sum(grid[1]) + sum(grid[2])
    grid[0][0] = s // 2 - sum(grid[0])
    grid[1][1] = s // 2 - sum(grid[1])
    grid[2][2] = s // 2 - sum(grid[2])

    for i in range(3):
        print(' '.join(list(map(str, grid[i]))))


main()
