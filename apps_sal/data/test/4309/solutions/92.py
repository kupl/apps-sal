def main():
    n = input()
    if n[0] == '0':
        print('111')
    elif n[0] < n[1] or n[0] < n[2]:
        print(((int(n[0]) + 1) * 111))
    else:
        print((int(n[0]) * 111))


def __starting_point():
    main()


__starting_point()
