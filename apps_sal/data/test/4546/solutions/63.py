# A - ι⊥l
def main():
    a, b, c = map(int, input().split())

    if b - a == c - b:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
