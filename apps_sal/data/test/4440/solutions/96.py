def answer(l: int) -> float:
    return pow(l / 3, 3)


def main():
    l = int(input())
    print(answer(l))


def __starting_point():
    main()


__starting_point()
