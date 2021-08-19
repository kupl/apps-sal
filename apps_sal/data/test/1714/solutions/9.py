def main():
    (n, k) = [int(x) for x in input().split()]
    for i in range(n):
        if k > 0:
            print(2 * i + 1, 2 * i + 2, end=' ')
            k -= 1
        else:
            print(2 * i + 2, 2 * i + 1, end=' ')


def __starting_point():
    main()


__starting_point()
