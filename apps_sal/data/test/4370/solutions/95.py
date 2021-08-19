def main():
    (a, b) = list(map(int, input().split()))
    if a <= 8 and b <= 8:
        print('Yay!')
    else:
        print(':(')


def __starting_point():
    main()


__starting_point()
