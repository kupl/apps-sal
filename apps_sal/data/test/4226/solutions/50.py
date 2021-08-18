def main():
    x, y = map(int, input().split())
    b = (y - x * 2) // 2
    a = x - b
    if a >= 0 and b >= 0 and 2 * a + 4 * b == y:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
