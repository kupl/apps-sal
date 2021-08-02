def main() -> None:
    a, b, c, k = list(map(int, input().split()))

    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print((a - (k - a - b)))
    return


def __starting_point():
    main()


__starting_point()
