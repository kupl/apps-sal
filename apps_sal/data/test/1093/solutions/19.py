def read_ints():
    return [int(x) for x in input(' ').split()]


def main():
    n, m = read_ints()
    field = [list(input()) for _ in range(n)]
    heights = [sum([1 if field[j][i] == '*' else 0 for j in range(n)]) for i in range(m)]
    INF = 1**10
    max_up = 0
    max_down = 0
    for i in range(m - 1):
        delta = heights[i + 1] - heights[i]
        max_up = max(max_up, delta)
        max_down = max(max_down, -delta)
    print(max_up, max_down)


def __starting_point():
    main()


__starting_point()
