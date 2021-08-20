def main():
    l = [list(map(int, input().split())) for _ in range(3)]
    s = sum(map(sum, l)) // 2
    for (i, row) in enumerate(l):
        row[i] = s - sum(row)
        print(*row)


def __starting_point():
    main()


__starting_point()
