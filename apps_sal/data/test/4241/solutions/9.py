def answer(s: str, t: str) -> int:
    result = len(t)
    for i in range(len(s) - len(t) + 1):
        count = 0
        for j in range(len(t)):
            if t[j] != s[i + j]:
                count += 1
        result = min(result, count)

    return result


def main():
    s = input()
    t = input()
    print((answer(s, t)))


def __starting_point():
    main()

__starting_point()
