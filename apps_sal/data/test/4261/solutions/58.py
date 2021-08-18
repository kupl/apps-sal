
def main():
    a, b, c = list(map(int, input().split()))
    print((0 if a - b >= c else c - (a - b)))


def __starting_point():
    main()


__starting_point()
