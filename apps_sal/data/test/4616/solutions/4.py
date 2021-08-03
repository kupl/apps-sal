import sys


def main():
    s = input()
    N = len(s)
    ans = s[0] + str(N - 2) + s[-1]
    print(ans)


def __starting_point():
    main()


__starting_point()
