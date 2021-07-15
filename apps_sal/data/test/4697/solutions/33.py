import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = list(map(int, readline().split()))

    if N >= M // 2:
        ans = M // 2
    else:
        ans = N
        L = M - 2 * N
        ans += L // 4

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
