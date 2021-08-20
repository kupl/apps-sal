def main():
    n = input()
    d = int(n[0])
    if d < 9:
        year = int(str(d + 1) + '0' * (len(n) - 1))
    else:
        year = int('1' + '0' * len(n))
    print(year - int(n))


def __starting_point():
    main()


__starting_point()
