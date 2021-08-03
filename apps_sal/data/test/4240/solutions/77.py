def answer(s: str, t: str) -> str:
    for _ in range(len(s)):
        if t == s:
            return 'Yes'
        s = s[-1] + s[:-1]
    return 'No'


def main():
    s = input()
    t = input()
    print((answer(s, t)))


def __starting_point():
    main()


__starting_point()
