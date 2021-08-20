import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X = int(readline())
    if X in (7, 5, 3):
        print('YES')
    else:
        print('NO')
    return


def __starting_point():
    main()


__starting_point()
