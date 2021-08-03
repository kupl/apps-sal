def main():
    s = input()
    if len(set(s)) == len(s):
        print('yes')
    else:
        print('no')


def __starting_point():
    main()


__starting_point()
