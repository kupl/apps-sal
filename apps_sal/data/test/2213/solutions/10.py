def main():
    n, m, k = map(int, input().split())
    print(m * (m - 1) // 2)
    for i in range(1, m):
        for j in range(i + 1, m + 1):
            print(j, i) if k else print(i, j)


def __starting_point():
    main()


__starting_point()
