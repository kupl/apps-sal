import sys


def is_vowel(c):
    return c in set("aeiouy")


def main():
    _ = input()
    s = input()

    for _ in range(len(s)):
        for i in range(len(s) - 1):
            if is_vowel(s[i]) and is_vowel(s[i + 1]):
                s = s[:(i + 1)] + s[(i + 2):]
                break

    print(s)


def __starting_point():
    main()


__starting_point()
