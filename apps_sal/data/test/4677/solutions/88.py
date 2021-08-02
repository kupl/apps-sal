def answer(s: str) -> str:
    result = ''
    for c in s:
        if c == 'B':
            result = result[:-1]
        else:
            result += c

    return result


def main():
    s = input()
    print((answer(s)))


def __starting_point():
    main()


__starting_point()
