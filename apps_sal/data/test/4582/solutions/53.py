def main():
    (a, b) = input().split()
    if a == 'H':
        if b == 'H':
            print('H')
        else:
            print('D')
    elif b == 'H':
        print('D')
    else:
        print('H')


def __starting_point():
    main()


__starting_point()
