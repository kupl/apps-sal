import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    x = list(map(int, input().split()))
    print(len(set(x)))


def __starting_point():
    main()


__starting_point()
