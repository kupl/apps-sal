def main():
    S = input()

    def first(s):
        return s == s[::-1]

    def second(s):
        n = len(s)
        return s[:(n - 1) // 2] == s[:(n - 1) // 2:-1]

    def third(s):
        n = len(s)
        temp = s[(n + 3) // 2 - 1:]
        return temp == temp[::-1]
    return 'Yes' if first(S) and second(S) and third(S) else 'No'


def __starting_point():
    print(main())


__starting_point()
