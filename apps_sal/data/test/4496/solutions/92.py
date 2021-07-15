import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    D = int(readline())

    if D == 25:
        ans = 'Christmas'
    elif D == 24:
        ans = 'Christmas Eve'
    elif D == 23:
        ans = 'Christmas Eve Eve'
    else:
        ans = 'Christmas Eve Eve Eve'

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
