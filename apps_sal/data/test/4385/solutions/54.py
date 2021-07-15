import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b, c, d, e, k = list(map(int, read().split()))

    if e - a > k:
        print(':(')
    else:
        print('Yay!')

    return


def __starting_point():
    main()

__starting_point()
