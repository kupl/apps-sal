import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    for x in range(N, 1000):
        if len(set(str(x))) == 1:
            print(x)
            return

    return


def __starting_point():
    main()

__starting_point()
