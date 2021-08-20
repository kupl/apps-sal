def main():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')


def __starting_point():
    main()


__starting_point()
