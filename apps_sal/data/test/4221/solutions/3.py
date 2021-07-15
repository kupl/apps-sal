def main():
    s = input()
    if s[-1] == 's':
        s += 'es'
    else:
        s += 's'
    print(s)


def __starting_point():
    main()


__starting_point()
