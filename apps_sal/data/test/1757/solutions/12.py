def main():
    n = int(input())
    name = ["o"] * n
    b, c = 1, 1
    while c <= n:
        name[c - 1] = 'O'
        b, c = c, b + c

    print(''.join(name))


def __starting_point():
    main()


__starting_point()
