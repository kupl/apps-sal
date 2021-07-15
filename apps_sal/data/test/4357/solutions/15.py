import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = list(map(int, readline().split()))
    A.sort()
    print((A[0] + A[1] + A[2] * 10))

    return


def __starting_point():
    main()

__starting_point()
