def main():
    x = int(input())
    n = 0
    i = 1
    while n < x:
        n += i
        i += 1
    print(i - 1)


def __starting_point():
    main()


__starting_point()
