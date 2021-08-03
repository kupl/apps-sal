import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    words = list(input().split())
    print((words[0][0] + words[1][0] + words[2][0]).upper())


def __starting_point():
    main()


__starting_point()
