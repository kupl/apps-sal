import sys
import os


def isVowel(x):
    return x == 'a' or x == 'e' or x == 'i' or (x == 'o') or (x == 'u')


def romaji(str):
    last = None
    for c in str:
        if last is None:
            last = c
            continue
        if not isVowel(last) and last != 'n' and (not isVowel(c)):
            return 'NO'
        last = c
    if not isVowel(last) and last != 'n':
        return 'NO'
    return 'YES'


def main():
    str = input()
    print(romaji(str))


def __starting_point():
    main()


__starting_point()
