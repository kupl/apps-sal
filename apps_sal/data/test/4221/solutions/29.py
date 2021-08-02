import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    print((s + "es" if s[-1] == "s" else s + "s"))


def __starting_point():
    main()


__starting_point()
