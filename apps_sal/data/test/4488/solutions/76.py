import sys
input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())
    if a > b:
        print('GREATER')
    elif a < b:
        print('LESS')
    elif a == b:
        print('EQUAL')


def __starting_point():
    main()


__starting_point()
