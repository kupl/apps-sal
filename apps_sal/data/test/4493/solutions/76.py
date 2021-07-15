def main():
    grid = [list(map(int, input().split())) for i in range(3)]
    all = sum(sum(grid, []))
    a = [0] * 3
    b = [0] * 3
    for i1 in range(0, grid[0][0] + 1):
        a[0] = i1
        b[0] = grid[0][0] - i1
        for j2 in range(0, grid[1][1] + 1):
            a[1] = j2
            b[1] = grid[1][1] - j2
            for k3 in range(0, grid[2][2] + 1):
                a[2] = k3
                b[2] = grid[2][2] - k3
                if (sum(a) * 3) + (sum(b) * 3) == all:
                    print("Yes")
                    return
    print('No')





def __starting_point():
    main()
__starting_point()
