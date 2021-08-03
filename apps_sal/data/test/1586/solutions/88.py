import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    if N % 2:
        print((0))
        return

    ans = 0
    N //= 2
    while N:
        N //= 5
        ans += N

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
