
def main():
    n = int(input())
    i = 0
    while 2 ** i <= n:
        i += 1
    print((2 ** (i - 1)))


def __starting_point():
    main()


__starting_point()
