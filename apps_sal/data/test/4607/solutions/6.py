def main():
    (a, b) = list(map(int, input().split()))
    if a <= b:
        print(a)
    else:
        print(a - 1)


def __starting_point():
    main()


__starting_point()
