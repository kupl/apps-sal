import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T, *t = list(map(int, read().split()))

    ans = 0
    for i in range(N - 1):
        if t[i] + T > t[i + 1]:
            ans += t[i + 1] - t[i]
        else:
            ans += T
    ans += T

    print(ans)

    return


def __starting_point():
    main()


__starting_point()
