def answer(s: str) -> int:
    count = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            count += 1

    return count


def main():
    s = input()
    print((answer(s)))


def __starting_point():
    main()

__starting_point()
