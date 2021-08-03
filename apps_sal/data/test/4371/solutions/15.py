def answer(s: str) -> int:
    return min(abs(753 - int(s[i:i + 3])) for i in range(len(s) - 2))


def main():
    s = input()
    print(answer(s))


def __starting_point():
    main()


__starting_point()
