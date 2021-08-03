def answer(o: str, e: str) -> str:
    result = ''
    e += ' '
    for i in range(len(o)):
        result += o[i] + e[i]

    return result.strip()


def main():
    o = input()
    e = input()
    print(answer(o, e))


def __starting_point():
    main()


__starting_point()
