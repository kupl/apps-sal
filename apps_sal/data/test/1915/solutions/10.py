def main():
    n = int(input())
    a = [[1] * n for _ in range(n)]
    for y in range(1, n):
        for x in range(1, n):
            a[y][x] = a[y - 1][x] + a[y][x - 1]
    print(a[-1][-1])


def __starting_point():
    main()
__starting_point()
