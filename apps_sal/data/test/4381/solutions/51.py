import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (X, Y) = list(map(int, readline().split()))
    print(X + Y // 2)
    return


def __starting_point():
    main()


__starting_point()
