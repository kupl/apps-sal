def answer(s: str) -> int:
    return s.rfind('Z') - s.find('A') + 1


def main():
    s = input()
    print((answer(s)))


def __starting_point():
    main()


__starting_point()
