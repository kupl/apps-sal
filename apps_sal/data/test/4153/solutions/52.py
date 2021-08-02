import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    red = S.count('0')
    blue = len(S) - red

    print((min(red, blue) * 2))

    return


def __starting_point():
    main()


__starting_point()
