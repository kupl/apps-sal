def main():
    n = int(input())
    grid = [input() for _ in range(n)]
    row_map = {}
    max_frequency = 0
    for row in grid:
        if row in row_map:
            row_map[row] += 1
        else:
            row_map[row] = 1
        max_frequency = max(max_frequency, row_map[row])
    print(max_frequency)


def __starting_point():
    main()


__starting_point()
