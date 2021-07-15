import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    if N % 2 == 0:
        print(N)
    else:
        print((2 * N))

    return


def __starting_point():
    main()

__starting_point()
