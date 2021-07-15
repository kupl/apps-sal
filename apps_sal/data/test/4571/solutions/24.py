import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = list(map(int, readline().split()))

    ans = ((N - M) * 100 + 1900 * M) * pow(2, M)

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
