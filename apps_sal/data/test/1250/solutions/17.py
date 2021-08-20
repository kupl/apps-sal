def main():
    n = int(input())
    if n <= 2:
        v = [-1]
    else:
        v = [int(i) for i in range(n, 0, -1)]
    print(*v, sep=' ')


def __starting_point():
    main()


__starting_point()
