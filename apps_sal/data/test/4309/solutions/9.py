import sys
input = sys.stdin.readline


def main():
    N = int(input())

    for i in range(N, 1111111):
        x = set(list(str(i)))
        if len(x) == 1:
            print(i)
            return


def __starting_point():
    main()


__starting_point()
