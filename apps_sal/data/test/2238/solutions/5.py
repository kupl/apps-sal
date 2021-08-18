
import re


def main():
    n = int(input())

    for x in range(n // 2):
        print('{0}{1}{0}'.format('*' * ((n - x * 2) // 2), 'D' * (x * 2 + 1)))

    for x in range(n // 2 + 1):
        print('{0}{1}{0}'.format('*' * x, 'D' * ((n - x * 2))))


def __starting_point():
    main()


__starting_point()
