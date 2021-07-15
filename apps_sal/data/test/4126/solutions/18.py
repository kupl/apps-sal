def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def answer(s: str) -> str:
    if not is_palindrome(s):
        return 'No'

    strings = [s[:(len(s) - 1) // 2], s[(len(s) + 3) // 2 - 1:]]
    for i in strings:
        if not is_palindrome(i):
            return 'No'

    return 'Yes'


def main():
    s = input()
    print((answer(s)))


def __starting_point():
    main()

__starting_point()
