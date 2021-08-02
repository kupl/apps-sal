
def main():
    x, y = list(map(int, input().split()))
    if x % y != 0:
        print((abs((x // y + 1) - (x // y))))
    else:
        print((abs((x // y) - (x // y))))


def __starting_point():
    main()


__starting_point()
