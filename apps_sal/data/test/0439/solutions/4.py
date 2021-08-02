import sys


def main():
    n = int(input())
    m = int(input())
    if n < 50:
        m = m % pow(2, n)

    print(m)


def __starting_point():
    main()


__starting_point()
