import sys
input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())

    if a == b:
        print("EQUAL")
    elif a > b:
        print("GREATER")
    else:
        print("LESS")


def __starting_point():
    main()


__starting_point()
