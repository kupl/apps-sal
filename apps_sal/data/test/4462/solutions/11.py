import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    m = sum(1 for a in A if a % 2 == 1)
    n2 = sum(1 for a in A if a % 2 == 0 and a % 4 != 0)
    n4 = sum(1 for a in A if a % 4 == 0)

    if m <= n4:
        print('Yes')
    elif m == n4 + 1:
        if n2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

    return


def __starting_point():
    main()


__starting_point()
