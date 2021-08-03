def main():
    print((sum((1 - (-1) ** i) // 2 if j == 'g' else (1 - (-1) ** i) // 2 - 1 for i, j in enumerate(input()))))


def __starting_point():
    main()


__starting_point()
