import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *TA = list(map(int, read().split()))

    x, y = 1, 1

    for t, a in zip(*[iter(TA)] * 2):
        m1 = (x + t - 1) // t
        m2 = (y + a - 1) // a
        m = max(m1, m2)
        x, y = t * m, a * m

    print((x + y))
    return


def __starting_point():
    main()


__starting_point()
